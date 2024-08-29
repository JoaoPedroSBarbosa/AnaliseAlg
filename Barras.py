import time
import random

# com memoização
def CorteBarrasMenor(P, n):
    LucrosMax = [0] * (n + 1)
    return CorteBarrasAux(P, n, LucrosMax)

def CorteBarrasAux(P, n, LucrosMax):
    if LucrosMax[n] > 0:
        return LucrosMax[n]

    if n == 1:
        LucrosMax[n] = P[n-1]
        return P[n-1]

    lucromax = P[n-1]

    for i in range(1, n):
        lucro = P[i-1] + CorteBarrasAux(P, n - i, LucrosMax)
        if lucro > lucromax:
            lucromax = lucro

    LucrosMax[n] = lucromax
    return lucromax

# abordagem iterativa
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

# Função para gerar entradas aleatórias e calcular o tempo médio de execução
def compara_algoritmos(max_tamanho, m):
    tamanhos = list(range(1, max_tamanho + 1))  
    tempos_memo = []
    tempos_item = []

    for n in tamanhos:
        tempo_memo = 0
        tempo_item = 0

        for _ in range(m):
            # Gera uma lista aleatória de lucros para tamanho n
            P = [random.randint(1, 100) for _ in range(n)]

            # Tempo de execução para memoização
            inicio_memo = time.time()
            CorteBarrasMenor(P, n)
            fim_memo = time.time()
            tempo_memo += fim_memo - inicio_memo

            # Tempo de execução para abordagem iterativa
            inicio_item = time.time()
            CorteBarrasItem(P, n)
            fim_item = time.time()
            tempo_item += fim_item - inicio_item

        # Calcula o tempo médio
        tempos_memo.append(tempo_memo / m)
        tempos_item.append(tempo_item / m)

    # Exibindo resultados
    for i, n in enumerate(tamanhos):
        print(f"Tamanho: {n} | Tempo médio (memoização): {tempos_memo[i]:.6f}s | Tempo médio (iterativa): {tempos_item[i]:.6f}s")

# teste
max_tamanho = 20  
m = 100  

compara_algoritmos(max_tamanho, m)
