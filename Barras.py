import time
import random
import matplotlib.pyplot as plt

def criarPrecos(tam):
    Precos = [0]
    while len(Precos) < tam:
        Precos.append(random.randint(1, tam * 10))

    Precos.sort()
    return Precos

# Função de memoização 
def CorteBarrasAux(P, n):
    Resultado = [0] * (n + 1)
    Cortes = [0] * (n + 1)
    CorteBarras(P, Resultado, n, Cortes)

def CorteBarras(P, Resultado, n, Cortes):
    if Resultado[n] != 0:
        return Resultado[n]

    if n == 1:
        Resultado[n] = P[n-1]
        Cortes[n] = 1
        return Resultado[n]

    lucroMax = P[n-1]  
    melhorCorte = n

    for i in range(1, n):
        lucro = P[i-1] + CorteBarras(P, Resultado, n - i, Cortes)  

        if lucro > lucroMax:
            lucroMax = lucro
            melhorCorte = i

    Resultado[n] = lucroMax
    Cortes[n] = melhorCorte

    return Resultado[n]

# Abordagem iterativa
def CorteBarrasItem(P, n):
    lmax = [0] * (n + 1)
    lmax[1] = P[0]

    for j in range(2, n + 1):
        lucromax = P[j - 1]
        for i in range(1, j):
            lucro = P[i - 1] + lmax[j - i]
            if lucro > lucromax:
                lucromax = lucro
        lmax[j] = lucromax

    return lmax[n]

# comparar os tempos de execução e gerar o gráfico
def compara_algoritmos(max_tamanho, m):
    tamanhos = list(range(1, max_tamanho + 1))  
    tempos_memo = []
    tempos_item = []

    for n in tamanhos:
        tempo_memo = 0
        tempo_item = 0

        for _ in range(m):
            P = criarPrecos(n)

            # memoização
            inicio_memo = time.time()
            CorteBarrasAux(P, n)
            fim_memo = time.time()
            tempo_memo += fim_memo - inicio_memo

            # abordagem iterativa
            inicio_item = time.time()
            CorteBarrasItem(P, n)
            fim_item = time.time()
            tempo_item += fim_item - inicio_item

        # tempo médio
        tempos_memo.append(tempo_memo / m)
        tempos_item.append(tempo_item / m)

    # resultados
    for i, n in enumerate(tamanhos):
        print(f"Tamanho: {n} | Tempo médio (memoização): {tempos_memo[i]:.6f}s | Tempo médio (iterativa): {tempos_item[i]:.6f}s")

    # Gerando o gráfico 
    plt.figure(figsize=(16, 4))
    plt.subplot(1, 2, 1)
    plt.plot(tamanhos, tempos_item, label='Iteração', marker='o')
    plt.plot(tamanhos, tempos_memo, label='Memoização', marker='o')
    plt.xlabel('Tamanho da Barra')
    plt.ylabel('Tempo Médio (microssegundos)')
    plt.legend(loc='lower right')
    plt.title('Comparação Métodos Memoização e Iteração')
    plt.grid(True)
    plt.show()

# Teste 
max_tamanho = 20  
m = 100  

compara_algoritmos(max_tamanho, m)
