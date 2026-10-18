import os

# Consultar funcionalidades do módulo "OS"
# no terminal: pyhton ->help ("os") ele entraga as funionalidades, mas tmb tem na pagina de documentação.

# 1 Retornar a pasta atual ultilizando "os"
print(os.getcwd)

# 2 Listar aquivos e pastas
print(os.listdir())

# 3 Versão do OS, nesse caso como ele vai ser executado no próprio terminal, mas se vc quiser testar no seu CMD tmb funciona
os.system("ver")

# 4 Configurações da Máquina
os.system("systeminfo")

# 5 Limpar a tela do terminal
os.system("cls")

# 6 Desligar o computador
## os.system("shutdown /s")    # <- ele desliga em 60s
## os.system("shutdown /s /t 0") <- ele desliga em 60s
os.system("shutdown /a")       # <- cancela o desligamento

def desligarEm1Hora():         # <- desligar em 1h
    os.system("shutdown /s /t 3600")

def desligarEm30Min():         # <- desligar em 30min   
    os.system("shutdown /s /t 1800")

def concelarDesligamento():
    os.system("shutdown /a")   # <- cancela o desligamento

concelarDesligamento()         # <- isso aqui impede que o sistema vá desligar, pois eu acabei de executar a função "def" pra cancelar.