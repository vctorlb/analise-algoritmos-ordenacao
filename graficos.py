# graficos.py
import matplotlib.pyplot as plt
import pandas as pd
import os

def gerar_e_salvar_graficos(resultados, diretorio_saida="resultados_graficos"):
    print("\n" + "="*50)
    print("GERANDO GRÁFICOS AGREGADOS E REFINADOS...")
    print("="*50)

    os.makedirs(diretorio_saida, exist_ok=True)

    df = pd.DataFrame(resultados)
    
    df_sucesso = df[df['status'] == 'Sucesso']

    tipos_ordem = df_sucesso['tipo_ordem'].unique()
    
    df_sucesso['nome_algoritmo_formatado'] = df_sucesso['nome_algoritmo_bruto'].apply(lambda x: x.replace('_', ' ').title())

    # Definir um estilo de plotagem (ex: 'seaborn-v0_8-darkgrid', 'ggplot', 'fivethirtyeight')
    plt.style.use('seaborn-v0_8-darkgrid') 

    # Cores personalizadas para os algoritmos (mais distintas)
    cores = plt.cm.get_cmap('tab10', len(df_sucesso['nome_algoritmo_formatado'].unique()))
    
    # Marcadores para as linhas
    marcadores = ['o', 's', '^', 'D', 'v', 'p', 'h', '*', 'X', 'P'] # Círculo, quadrado, triângulo, diamante, etc.

    for tipo_ordem in tipos_ordem:
        fig, ax = plt.subplots(figsize=(14, 8)) # Cria figura e eixos explicitamente
        subconjunto = df_sucesso[df_sucesso['tipo_ordem'] == tipo_ordem]
        
        algoritmos_unicos = subconjunto['nome_algoritmo_formatado'].unique()
        for i, nome_algoritmo in enumerate(algoritmos_unicos):
            dados_algoritmo = subconjunto[subconjunto['nome_algoritmo_formatado'] == nome_algoritmo]
            dados_algoritmo = dados_algoritmo.sort_values(by='n') 
            
            if not dados_algoritmo.empty:
                ax.plot(dados_algoritmo['n'], dados_algoritmo['tempo_ms'], 
                        label=nome_algoritmo, 
                        color=cores(i), # Usa a cor da paleta
                        marker=marcadores[i % len(marcadores)], # Cicla pelos marcadores
                        markersize=6, # Tamanho do marcador
                        linewidth=2) # Espessura da linha
            else:
                print(f"Aviso: Nenhum dado de sucesso para {nome_algoritmo} na ordem {tipo_ordem}.")

        # Título e Rótulos
        ax.set_title(f'Tempo de Execução dos Algoritmos de Ordenação - Lista {tipo_ordem.capitalize()}', 
                     fontsize=16, fontweight='bold')
        ax.set_xlabel('Tamanho da Lista (n)', fontsize=12)
        ax.set_ylabel('Tempo de Processamento (ms)', fontsize=12)

        # Configurações de Eixo (opcional, remova ou ajuste se quiser auto-scaling)
        # ax.set_ylim(bottom=0) # Garante que o eixo Y comece em zero ou um valor razoável

        # Legenda
        ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), 
                  borderaxespad=0., fontsize=10, frameon=True, shadow=True, borderpad=1)
        
        # Grid
        ax.grid(True, linestyle='--', alpha=0.7)

        # Remover bordas desnecessárias para um visual mais limpo
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # Ajusta o layout para evitar que a legenda se sobreponha
        plt.tight_layout(rect=[0, 0, 0.88, 1]) 
        
        nome_arquivo = os.path.join(diretorio_saida, f'grafico_tempo_execucao_agregado_{tipo_ordem}_refinado.png')
        plt.savefig(nome_arquivo, dpi=300) # Salva com alta resolução
        print(f"Gráfico salvo: {nome_arquivo}")
        plt.close(fig) # Fecha a figura para liberar memória