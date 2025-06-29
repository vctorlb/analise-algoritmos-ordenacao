# Relatório de Análise de Algoritmos de Ordenação

**Disciplina:** Projeto e Análise de Algoritmos (PAA)

---

## 📄 Descrição do Projeto

Este projeto é um trabalho da disciplina de Projeto e Análise de Algoritmos (PAA) que visa analisar o comportamento de diversos algoritmos de ordenação. O estudo compara o tempo de execução de sete algoritmos: Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Counting Sort e Radix Sort. A análise é realizada sob três cenários distintos de ordenação de lista inicial: aleatória, crescente e decrescente.

Os testes foram conduzidos com listas de tamanhos variando de $N=10$ a $N=200$, em incrementos de 10. Para cada algoritmo, foram utilizadas instâncias de lista base específicas, conforme especificado na atividade. Os resultados de tempo de execução são apresentados de forma clara em gráficos comparativos.

## 🎯 Propósito

O principal objetivo deste projeto é fornecer uma comparação prática e detalhada do desempenho dos algoritmos de ordenação implementados. Através da medição precisa do tempo de execução em diferentes cenários de entrada de dados (listas aleatórias, crescentes e decrescentes), buscamos:

* Validar as complexidades de tempo teóricas dos algoritmos ($O(N^2)$, $O(N \log N)$, $O(N+K)$, $O(d(N+K))$).

* Entender como a ordem inicial dos dados impacta significativamente a eficiência de cada algoritmo.

O relatório final, derivado desta análise, oferece insights valiosos para a escolha mais adequada de um algoritmo de ordenação, considerando o tipo e o volume de dados a serem processados.

## 🚀 Como Executar o Projeto

Para executar este projeto em seu ambiente local e replicar a análise de desempenho dos algoritmos de ordenação, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado em seu sistema. As bibliotecas Python necessárias para a execução do projeto são `matplotlib` (para geração de gráficos) e `pandas` (para manipulação de dados).

Você pode instalá-las facilmente usando o `pip`, o gerenciador de pacotes do Python:

```bash
pip install matplotlib pandas

### Estrutura do Projeto

O código-fonte do projeto está modularizado para garantir clareza e manutenção, organizado nos seguintes arquivos:

* `algoritmos.py`: Contém as implementações detalhadas de todos os algoritmos de ordenação em estudo (Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Counting Sort, Radix Sort).
* `utilidades.py`: Inclui funções auxiliares essenciais para o projeto, como a preparação de listas de teste em diferentes formatos (aleatória, crescente, decrescente) e a medição precisa do tempo de execução de cada algoritmo.
* `graficos.py`: Responsável pela lógica de geração e salvamento dos gráficos de tempo de execução, que visualizam o desempenho dos algoritmos ao longo dos testes.
* `principal.py`: Este é o script principal do projeto. Ele orquestra todo o fluxo de execução, chamando as funções dos outros módulos para realizar os testes de desempenho, coletar os dados e gerar os gráficos finais.

### Passos para Execução

1.  **Navegue até o diretório do projeto:**
    Abra seu terminal ou prompt de comando. Use o comando `cd` para navegar até a pasta raiz onde você clonou ou salvou os arquivos deste projeto:

    ```bash
    cd /caminho/para/analise-algoritmos-ordenacao
    ```
    (Substitua `/caminho/para/analise-algoritmos-ordenacao` pelo caminho real da sua pasta).

2.  **Execute o script principal:**
    Com o terminal posicionado na pasta do projeto, execute o script `principal.py` usando o interpretador Python:

    ```bash
    python principal.py
    ```

3.  **Verifique os resultados:**
    Após a conclusão da execução (que pode levar alguns instantes, dependendo do desempenho do seu sistema), os gráficos gerados serão automaticamente salvos em um novo diretório chamado `resultados_graficos` (ou nome similar, configurado no código) localizado na raiz do projeto. Você pode então abrir esses arquivos de imagem (`.png` ou `.svg`) para visualizar a análise de desempenho de cada algoritmo.

## 📚 Algoritmos Implementados e Complexidade

Detalhes sobre os algoritmos de ordenação implementados e suas complexidades de tempo teóricas:

* **Bubble Sort:** $O(N^2)$ no pior e caso médio, $O(N)$ no melhor caso.
* **Insertion Sort:** $O(N^2)$ no pior e caso médio, $O(N)$ no melhor caso.
* **Merge Sort:** $O(N \log N)$ em todos os casos (melhor, médio, pior).
* **Quick Sort:** $O(N \log N)$ no caso médio e melhor caso, $O(N^2)$ no pior caso (com estratégia de pivô "mediana de três").
* **Heap Sort:** $O(N \log N)$ em todos os casos (melhor, médio, pior).
* **Counting Sort:** $O(N+K)$, onde $K$ é o intervalo dos valores. Algoritmo de ordenação não comparativa, ideal para inteiros não negativos.
* **Radix Sort:** $O(d(N+K))$, onde $d$ é o número de dígitos e $K$ a base. Algoritmo de ordenação não comparativa, também para inteiros não negativos.

## 📊 Análise dos Resultados

Os gráficos gerados neste projeto fornecem uma validação visual e prática das características teóricas de cada algoritmo:

* **Algoritmos $O(N^2)$ (Bubble Sort, Insertion Sort):** Confirmam sua ineficiência para listas grandes nos cenários de pior e médio caso (listas aleatórias e decrescentes), demonstrando um crescimento exponencial do tempo de execução. No entanto, exibem um excelente desempenho no melhor caso (listas crescentes) devido a otimizações inerentes.

* **Algoritmos $O(N \log N)$ (Merge Sort, Heap Sort, Quick Sort):**
    * **Merge Sort** e **Heap Sort** se mostram consistentemente robustos e eficientes em todos os cenários, sem as flutuações e picos de pior caso observados no Quick Sort. Sua performance é previsível e escalável.
    * O **Quick Sort** demonstra sua volatilidade característica; embora seja notavelmente rápido no caso médio, suas instâncias de pior caso (como listas já ordenadas ou inversamente ordenadas, dependendo da estratégia de pivô) são claramente visíveis nos gráficos com picos significativos de tempo de execução.

* **Algoritmos de Tempo Linear (Counting Sort, Radix Sort):** Para os dados numéricos e dentro de suas restrições de uso (inteiros não negativos com um intervalo $K$ razoável), esses algoritmos são, de longe, os mais rápidos. Eles apresentam tempos de execução quase constantes ou com um crescimento muito suave, superando todos os algoritmos baseados em comparação para este tipo de entrada.
