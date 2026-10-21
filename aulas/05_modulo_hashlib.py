## Módulo HashLib serve para criptografia de textos, existem Bibliotecas/ Módulos externos melhores e mais robustas
import hashlib

# 1 Verificar algoritimos disponíveis
print(hashlib.algorithms_available)

# 2 Verificar algoritimos de acordo com o SO (Sistema Operacional)
print(hashlib.algorithms_guaranteed)

# 3 Utilizando o SHA256
algoritimo = hashlib.sha256()
print(algoritimo.digest())

mensagem = "A melhor forma de prever o futuro é, criá-lo".encode() ### <- é preciso por o ".encode()"
algoritimo.update(mensagem)
print(algoritimo.hexdigest())

# 4 Utilizando o MD5 - uma hash que é mais utilizada para verificar a indegridade de dados
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest()) #<- fica em uvalor criptografado menor