# Modulo "math" na prática. 
# OBS: existem outras bibliotecas externas do python que são bem melhores para realizar operações matemáticas.

import math

# 1 Acessar o número PI
print(math.pi)
print(f"{math.pi:.2f}") # <- para deixar em 2 casas decimais (comumente vemos ele assim)

# 2 Acessar o número de Euler
print(math.e) 
print(f"{math.e:.2f}")  # <- para deixar em 2 casas decimais (comumente vemos ele assim)

# 3 Arredondamento de números para cima e para baixo
num = 8.8
print(math.ceil(num))  # <- Areddondadno apra cima 
print(math.floor(num)) # <- Areddondadno apra baixo

# 4 Fatorial de um número
num2 = int(input("Digite um número: "))
print(math.factorial(num2)) # <- "Função" que já existe dentro da protpia biblioteca nativa do "math"

# 5 Potência de números
print(math.pow(5, 5))

# 6 Raiz quadrada de um número
print(math.sqrt(169))

# 7 Máximo Divisor Comum (MDC)
mdc = math.gcd(20, 100) # <- Demosntração do menor divizor comum entre (x, y)
print(mdc)

# 8 Logaritimo (ou ln)
print(math.log(10))