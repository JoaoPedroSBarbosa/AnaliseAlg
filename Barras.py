import time

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

# usando recursão 
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


P = [1, 5, 8, 9, 10, 17, 17, 20]  # Lucro para tamanhos 1, 2, 3, 4, 5, 6, 7, 8
n = len(P)  # Tamanho da barra inicial

# Medindo o tempo de execução da solução com memoização
inicio_memo = time.time()
lucro_maximo_memo = CorteBarrasMenor(P, n)
fim_memo = time.time()

# Medindo o tempo de execução da solução recursiva
inicio_rec = time.time()
lucro_maximo_rec = CorteBarrasItem(P, n)
fim_rec = time.time()

# Exibindo os resultados e os tempos
print(f'O lucro máximo (memoização) é: {lucro_maximo_memo}')
print(f'Tempo de execução (memoização): {fim_memo - inicio_memo:.6f} segundos')

print(f'O lucro máximo (recursão) é: {lucro_maximo_rec}')
print(f'Tempo de execução (recursão): {fim_rec - inicio_rec:.6f} segundos')
