# Relatório de Análise de Algoritmos de Ordenação

---

### Contexto do Projeto

* **Disciplina:** Projeto e Análise de Algoritmos (PAA)
---

## 📄 Descrição do Projeto

Este projeto é um trabalho da disciplina de Projeto e Análise de Algoritmos (PAA) com o objetivo de analisar o comportamento de diversos algoritmos de ordenação. O estudo compara o tempo de execução de sete algoritmos distintos: **Bubble Sort**, **Insertion Sort**, **Merge Sort**, **Quick Sort**, **Heap Sort**, **Counting Sort** e **Radix Sort**. A análise é conduzida sob três cenários distintos de ordenação de lista inicial: aleatória (formato original), crescente e decrescente.

Os testes foram realizados com listas de tamanhos que variam de $N=10$ a $N=200$, em incrementos de 10. Para cada algoritmo, foram utilizadas instâncias de lista base específicas, conforme detalhado na atividade. Os resultados de tempo de execução são apresentados de forma clara e concisa em gráficos comparativos.

## 🎯 Propósito

O principal objetivo deste projeto é fornecer uma comparação prática e detalhada do desempenho dos algoritmos de ordenação implementados. Através da medição precisa do tempo de execução em diferentes cenários de entrada de dados (listas aleatórias, crescentes e decrescentes), buscamos:

* Validar as complexidades de tempo teóricas dos algoritmos, como $O(N^2)$, $O(N \log N)$, $O(N+K)$ e $O(d(N+K))$.
* Compreender como a ordem inicial dos dados impacta significativamente a eficiência de cada algoritmo.

O relatório final, resultante desta análise, oferece *insights* valiosos para a escolha mais adequada de um algoritmo de ordenação, considerando o tipo e o volume de dados a serem processados em diferentes aplicações.

## 🚀 Como Executar o Projeto

Para executar este projeto em seu ambiente local e replicar a análise de desempenho dos algoritmos de ordenação, siga os passos detalhados abaixo:

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado em seu sistema. As bibliotecas Python necessárias para a execução do projeto são `matplotlib` (para geração de gráficos) e `pandas` (para manipulação de dados).

Você pode instalá-las facilmente usando o `pip`, o gerenciador de pacotes do Python:

```bash
pip install matplotlib pandas
