# algoritmos.py

def bubble_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("Bubble Sort requer uma lista como entrada.")
    if len(lista) <= 1:
        return lista[:] # Retorna uma cópia para garantir consistência

    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n - i - 1):
            # Tenta comparar elementos, captura TypeError se não forem comparáveis
            try:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocado = True
            except TypeError:
                raise TypeError(f"Elementos da lista não são comparáveis por Bubble Sort: {lista[j]} e {lista[j+1]}")
        if not trocado:
            break
    return lista

def insertion_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("Insertion Sort requer uma lista como entrada.")
    if len(lista) <= 1:
        return lista[:]

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        try:
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        except TypeError:
            raise TypeError(f"Elementos da lista não são comparáveis por Insertion Sort: {chave} e {lista[j]}")
    return lista

def merge_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("Merge Sort requer uma lista como entrada.")
    if len(lista) <= 1:
        return lista[:]

    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0
        
        try:
            while i < len(metade_esquerda) and j < len(metade_direita):
                if metade_esquerda[i] < metade_direita[j]:
                    lista[k] = metade_esquerda[i]
                    i += 1
                else:
                    lista[k] = metade_direita[j]
                    j += 1
                k += 1
        except TypeError:
            raise TypeError("Elementos da lista não são comparáveis por Merge Sort.")

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1
    return lista

# Função auxiliar para o Quick Sort
def _particionar(lista, baixo, alto):
    # Escolhe o pivô: estratégia "mediana de três" para maior robustez contra pior caso
    # Garante que lista[baixo], lista[meio], lista[alto] são comparáveis
    try:
        meio = (baixo + alto) // 2
        if lista[baixo] > lista[meio]:
            lista[baixo], lista[meio] = lista[meio], lista[baixo]
        if lista[baixo] > lista[alto]:
            lista[baixo], lista[alto] = lista[alto], lista[baixo]
        if lista[meio] > lista[alto]:
            lista[meio], lista[alto] = lista[alto], lista[meio]
        
        # Coloca o pivô (agora lista[meio]) no final para a partição padrão
        lista[meio], lista[alto] = lista[alto], lista[meio]
        pivo = lista[alto]
    except TypeError:
        raise TypeError("Elementos da lista não são comparáveis por Quick Sort.")

    i = baixo - 1

    for j in range(baixo, alto):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

# Quick Sort com implementação iterativa (não recursiva)
def quick_sort(lista, baixo=0, alto=None):
    if not isinstance(lista, list):
        raise TypeError("Quick Sort requer uma lista como entrada.")
    if len(lista) <= 1:
        return lista[:]

    if alto is None:
        alto = len(lista) - 1
    
    pilha = []
    pilha.append((baixo, alto))

    while pilha:
        baixo_atual, alto_atual = pilha.pop()

        if baixo_atual < alto_atual:
            # A função _particionar agora lida com erros de comparação
            indice_pivo = _particionar(lista, baixo_atual, alto_atual)

            # Adiciona os sub-arrays à pilha para processamento futuro
            # Prioriza o menor sub-array para otimização de espaço na pilha
            if indice_pivo - 1 - baixo_atual > alto_atual - (indice_pivo + 1): # Se o lado esquerdo for maior
                if indice_pivo + 1 < alto_atual:
                    pilha.append((indice_pivo + 1, alto_atual))
                if indice_pivo - 1 > baixo_atual:
                    pilha.append((baixo_atual, indice_pivo - 1))
            else: # Se o lado direito for maior ou igual
                if indice_pivo - 1 > baixo_atual:
                    pilha.append((baixo_atual, indice_pivo - 1))
                if indice_pivo + 1 < alto_atual:
                    pilha.append((indice_pivo + 1, alto_atual))
    return lista

class _AuxiliarHeapSort:
    def ordenar(self, vetor):
        if not isinstance(vetor, list):
            raise TypeError("Heap Sort Helper requer uma lista como entrada.")
        if len(vetor) <= 1:
            return # A lista já está ordenada ou vazia, não precisa de heapificação

        self.__construir_max_heap(vetor)
        tamanho = len(vetor) - 1
        for s in range(tamanho, 0, -1):
            try:
                vetor[0], vetor[s] = vetor[s], vetor[0]
            except TypeError:
                raise TypeError(f"Elementos da lista não são comparáveis por Heap Sort: {vetor[0]} e {vetor[s]}")
            self.__heapificar(vetor, 0, s - 1)
    
    def __construir_max_heap(self, vetor):
        tamanho = len(vetor) - 1
        for n in range(tamanho // 2, -1, -1):
            self.__heapificar(vetor, n, tamanho)

    def __heapificar(self, vetor, raiz, ultimo):
        esquerda = raiz * 2 + 1
        direita = raiz * 2 + 2
        maior = raiz

        try:
            if esquerda <= ultimo and vetor[esquerda] > vetor[maior]:
                maior = esquerda

            if direita <= ultimo and vetor[direita] > vetor[maior]:
                maior = direita
        except TypeError:
            raise TypeError("Elementos da lista não são comparáveis por Heap Sort.")

        if maior != raiz:
            vetor[raiz], vetor[maior] = vetor[maior], vetor[raiz]
            self.__heapificar(vetor, maior, ultimo)

def heap_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("Heap Sort requer uma lista como entrada.")
    if len(lista) <= 1:
        return lista[:]

    ordenador = _AuxiliarHeapSort()
    ordenador.ordenar(lista)
    return lista

def counting_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("CountingSort requer uma lista como entrada.")
    if not lista: # Lista vazia
        return []
    
    # Validação rigorosa: todos os elementos devem ser inteiros e não negativos
    if not all(isinstance(x, int) for x in lista):
        raise TypeError("CountingSort requer que todos os elementos da lista sejam inteiros.")

    max_val = max(lista)
    min_val = min(lista)
    
    if min_val < 0:
        raise ValueError("CountingSort nesta implementação não suporta números negativos.")

    tamanho_array_contagem = max_val - min_val + 1
    array_contagem = [0] * tamanho_array_contagem
    
    for numero in lista:
        array_contagem[numero - min_val] += 1
        
    for i in range(1, tamanho_array_contagem):
        array_contagem[i] += array_contagem[i-1]
        
    ordenada = [0] * len(lista)
    for i in reversed(range(len(lista))):
        ordenada[array_contagem[lista[i] - min_val] - 1] = lista[i]
        array_contagem[lista[i] - min_val] -= 1
        
    return ordenada

def _counting_sort_para_radix(lista, expoente):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10
    
    for i in range(n):
        indice = lista[i] // expoente
        contagem[indice % 10] += 1
        
    for i in range(1, 10):
        contagem[i] += contagem[i-1]
        
    i = n - 1
    while i >= 0:
        indice = lista[i] // expoente
        saida[contagem[indice % 10] - 1] = lista[i]
        contagem[indice % 10] -= 1
        i -= 1
        
    for i in range(n):
        lista[i] = saida[i]

def radix_sort(lista):
    if not isinstance(lista, list):
        raise TypeError("RadixSort requer uma lista como entrada.")
    if not lista: # Lista vazia
        return []

    # Validação rigorosa: todos os elementos devem ser inteiros e não negativos
    if not all(isinstance(x, int) and x >= 0 for x in lista):
        raise TypeError("RadixSort requer que todos os elementos da lista sejam inteiros e não negativos.")
        
    max_num = max(lista)
        
    expoente = 1
    while max_num // expoente > 0:
        _counting_sort_para_radix(lista, expoente)
        expoente *= 10
    return lista