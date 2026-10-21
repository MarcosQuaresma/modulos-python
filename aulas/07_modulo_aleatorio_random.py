# Modulo Random, ou Modulo Alatorio
import random

# 1 Selecionar valor aleatório de uma lista
lista1 = [7, 6, 4, 5, 1]
print(random.choice(lista1))  

# 2 Gerar um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 Sortear um caractere aleatório de um string
nome = "Curso Pyhon" 
r2 = random.choice(nome)
print(r2)

# 4 Seleciona mais de um valor aleatório -> random.sample(sequnecia, tamanho)
print(random.sample(lista1, 2))
print(random.sample(lista1, 3))
print(random.sample(nome, 2))

# 5 Programa de sorteio
done = False
while not done:
    print("O que você deseja fazer?\n digite '1' pra advinhar um número\n Digite '2' para sair")

    escolha = input(">")
    if escolha == "1":
        print("----------- Advinhe um número de 1 a 10 ----------- \n")
        numero = int(input("Digite um número de 1 a 10: "))
        resultado = random.randint(1, 10)
        if numero == resultado:
            print("Parabéns, você é um aspirante a cigano!")
        else:
            print(f"O número sorteado foi {resultado}, não foi dessa vez...Tente novamente") 
    elif escolha == "2":
        done = True 
    else:
        print("Opçao inválida. Escolha a opção 1 ou 2 ")