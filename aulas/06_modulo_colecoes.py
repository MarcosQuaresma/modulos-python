# O Modulo Coleções ou Collections, tem como objetivo estender um pouco mais as estruturas de dadso que nós vimos
from collections import Counter, namedtuple, deque
from operator import itemgetter # ultilizaremos do modulo "operator" o "itemgetter" a titulo de demonstração

# 1  Lista de Frutas (contagem) sem utilizar "for in" ou nenhum tipo de looping
frutas = ["Banana", "Uva", "Maçã", "Pêra", "Kiwi", "Amora",
          "Uva", "Manga", "Manga", "Abacaxi", "Laranja",
            "Kiwi", "Maçã", "Banana", "Amora", "Tangerina"]
print(frutas)
print(Counter(frutas))

# 2 Utilizando uma Tupla nomeada (é quase uma {} como dicionário)
game = namedtuple("game", ["nome", "preço", "nota" ])
g1 = game("BF6", 200, 9.9)
g2 = game("Fortnite", 0, 5.0)
g3 = game("Valorant", 0, 2.0)
g4 = game("CSGO2", 0, 9.9)
g5 = game("Arma 3", 120, 8.7)
print(f"{g1}\n {g2}\n {g3}\n {g4}\n {g5}\n")

# 3 Ordenando dicionários
estudantes = {"Marcos": 25, "Gabriela": 24, "Sophia": 18, "Bruno": 20}
a = sorted(estudantes.items(), key = itemgetter(0)) # (1) ele começa pelo menor item, (0) vai começar por ordem alfabetica
print(a)

# 4 Utilizando uma fila em ambas extremidades
fila = deque([20, 40, 60, 80])
fila.appendleft(10)
print(fila)
fila.appendleft(90)
fila.popleft()
fila.pop
print(fila)