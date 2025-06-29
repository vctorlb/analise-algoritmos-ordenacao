# utilidades.py
import time
import random

def executar_algoritmo_ordenacao(funcao_algoritmo, lista_entrada):
    lista_copia = lista_entrada.copy()

    tempo_inicio = time.perf_counter()
    tempo_processamento = None
    lista_ordenada = []
    status = "Falhou"
    mensagem_erro = None

    try:
        lista_ordenada = funcao_algoritmo(lista_copia)
        tempo_fim = time.perf_counter()
        tempo_processamento = (tempo_fim - tempo_inicio) * 1000
        status = "Sucesso"
    except Exception as e:
        status = "Falhou"
        mensagem_erro = str(e)
        
    nome_algoritmo_bruto = funcao_algoritmo.__name__
    lista_exibicao = str(lista_ordenada[:15]) + '...' if len(lista_ordenada) > 15 else str(lista_ordenada)
    
    print(f"- {nome_algoritmo_bruto.replace('_', ' ').title()}:")
    print(f"  -> Status: {status}")
    print(f"  -> Tempo: {tempo_processamento:.6f} ms" if tempo_processamento is not None else "  -> Tempo: N/A (Falhou)")
    if status == "Falhou":
        print(f"  -> Erro: {mensagem_erro}")
    print(f"  -> Lista Ordenada (primeiros 15): {lista_exibicao}")
    
    return {
        "nome_algoritmo_bruto": nome_algoritmo_bruto,
        "tempo_ms": tempo_processamento,
        "status": status,
        "mensagem_erro": mensagem_erro,
        "lista_ordenada_previa": lista_exibicao
    }

def preparar_lista_teste(instancia_base, n, tipo_ordem):
    tamanho_base = len(instancia_base)
    lista_teste = instancia_base * ((n // tamanho_base) + 1)
    lista_teste = lista_teste[:n]

    if tipo_ordem == "aleatoria":
        random.shuffle(lista_teste)
    elif tipo_ordem == "crescente":
        lista_teste.sort()
    elif tipo_ordem == "decrescente":
        lista_teste.sort(reverse=True)
    
    return lista_teste