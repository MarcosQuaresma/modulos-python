# Módulo Regular Expression, ou Módulo de Expressões Regulares

import re
txt = "Udemy uma plataforma de muitos cursos"
# 1 A títulod e mapeamento, teremos índice Inidical e índice Final de palavras
# O "r" significa um raw string (string bruta)

correspondeA = re.search(r"muitos cursos", txt) # o trecho "muitos cursos" é onde eu quero achar na variavel "txt"

print(f"Índice Inicial: {correspondeA.start()}") # corresponde a qual indice inicia a frase
print(f"Índice Final: {correspondeA.end ()}")    # corresponde a qual indice finaliza a frase

## UTILIDADE: evita contagem manual, com um módulo nativo o "re" de Expressões Regulares

# 2 Buscando o Índice que possui o ponto
site = "https://udemy.com"

correspondeA = re.search(r"\.", site) # nessesárioq eu se use o contra barra "\"(AltGr+9+2, no teclado numérico)
print(correspondeA)

# 3 Buscar uma lista de caracteres dentro de um frase, nesse caso na variável "txt"
padrao = "[g-m]"
reusltado = re.findall(padrao, txt) # nesse caso ele vai buscar o padrão definido em "padrao" no texto definido em "txt"
print(reusltado) 

# 4 Verificando o início de uma string com "for x in y"
regra = r"^A"
frase = ["A casa esta limpa", "O chão esta seujo", "A ciade esta limpa"]

for regras in frase:
    if re.match(regra, regras):
        print(f"Corresponde: {regras}")
    else:
        print(f"Não Corresponde: {regras}")

# Verificando o final de ums string
regraFinal = r"!$"
frase2 = "A madrugada esta quieta!"
correspondeA = re.search(regraFinal, frase2)

if correspondeA:
    print(f"Sim a frase {frase2}, corresponde com a regra")
else:
    print(f"Não, a frase {frase2} não corresponde com a regra")

