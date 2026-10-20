## Módulo "statistics" na prática
import statistics

# 1 Aplicando a Média
print(statistics.mean([3, 4, 5, 8, 9]))

# 2 Aplicando a mediana (ela se oraniza automatiamente dentro do calculo, do menor para o maior)

print(statistics.median([1, 3, 5, 8])) # na mediana par (quantidade de itens na lsita) somamos os 2 do meio da lsita e dividi por 2
print(statistics.median([3, 4, 4, 5, 6, 7, 7])) # na mediana impar (quantidade de itens na lista) a mediana é o númeor que fica no meio

# 3 Aplicando a moda (o valor que mais se repete)
print(statistics.mode([3, 4, 4, 5, 6, 7, 4, 7]))

# 4 Desvio padrão
## quanto mais próximo de Zero for o desvio padrão
## significa que os dadso do conjunto estão dispersos

print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))