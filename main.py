# principal.py
import sys
import os

sys.path.append(os.path.dirname(__file__))

from algoritmos import (
    bubble_sort, insertion_sort, merge_sort, 
    quick_sort, heap_sort, counting_sort, radix_sort
)
from utils import executar_algoritmo_ordenacao, preparar_lista_teste
from graficos import gerar_e_salvar_graficos

def executar_atividade_principal():
    instancias_algoritmos = {
        "BubbleSort": {
            "funcao": bubble_sort,
            "instancia_base": [-5, 42, 29, -19, -88, -98, -74, 0, 64, -26]
        },
        "InsertionSort": {
            "funcao": insertion_sort,
            "instancia_base": ['V', 'I', 'C', 'T', 'O', 'R', 'M', 'A', 'N', 'O']
        },
        "MergeSort": {
            "funcao": merge_sort,
            "instancia_base": [20, 84, 15, 58, 34, 21, 62, 33, 48, 74]
        },
        "QuickSort": {
            "funcao": quick_sort,
            "instancia_base": [93, 25, 26, 90, 57, 16, 84, 16, 13, 64] 
        },
        "HeapSort": { 
            "funcao": heap_sort,
            "instancia_base": [93, 25, 26, 90, 57, 16, 84, 16, 13, 64] # Usando a mesma do QuickSort
        },
        "CountingSort": {
            "funcao": counting_sort,
            # Instância compatível: apenas inteiros não negativos.
            # Se for testado com dados incompatíveis, o algoritmo lançará um TypeError/ValueError.
            "instancia_base": [0, 0, 0, 4, 4, 5, 2, 1, 6, 0] 
        },
        "RadixSort": {
            "funcao": radix_sort,
            # Instância compatível: apenas inteiros não negativos.
            "instancia_base": [83140, 64117, 17218, 93964, 65331, 50824, 65415, 39169, 86120, 87647]
        },
    }

    print("\n" + "="*50)
    print("INICIANDO TESTES DE ALGORITMOS DE ORDENAÇÃO")
    print("Cada algoritmo será testado com sua instância base específica.")
    print("="*50)

    tipos_ordem = ["aleatoria", "crescente", "decrescente"] 
    todos_resultados = []

    for nome_exibicao_algo, info_algo in instancias_algoritmos.items():
        funcao_algo = info_algo["funcao"]
        instancia_base = info_algo["instancia_base"]

        print(f"\n\n>>> Testando Algoritmo: {nome_exibicao_algo} com instância base: {instancia_base} <<<")

        for tipo_ordem in tipos_ordem:
            for n in range(10, 201, 10):
                lista_teste = preparar_lista_teste(instancia_base, n, tipo_ordem)

                print(f"\n--- Testando {nome_exibicao_algo} (n={n}, Ordem={tipo_ordem.upper()}) ---")
                print(f"Lista de Entrada (primeiros 15): {lista_teste[:15]}...")
                
                # A função 'executar_algoritmo_ordenacao' irá capturar quaisquer TypeErrors/ValueErrors
                # lançados pelos algoritmos e reportá-los como 'Falhou'.
                resultado = executar_algoritmo_ordenacao(funcao_algo, lista_teste.copy())
                if resultado: 
                    resultado["n"] = n
                    resultado["tipo_ordem"] = tipo_ordem
                    todos_resultados.append(resultado)
    
    print("\n" + "="*50)
    print("TESTES CONCLUÍDOS!")
    print("="*50)

    gerar_e_salvar_graficos(todos_resultados)


if __name__ == "__main__":
    executar_atividade_principal()