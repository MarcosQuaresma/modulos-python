# PROGRAMA PRINCIPAL

import operacoes_matematicas # em alguns casos importar um módulo completo pode não ser eficiente, pois ele é muito grande e não
                             # iriamos uasar ele por completo.
# Dentro do Módulo podemos importar também ultilizando o "from" somente o que é nescessário. como por exemplo:
from operacoes_matematicas import multiplicar, dividir

import str_utils # poderia importar separado ou completo.

print(operacoes_matematicas.somar(5, 4))    #<--- importanto do módulo INTEIRO de "operacoes_matematicas"
print(operacoes_matematicas.subtrair(5, 4)) #<--- importanto do módulo INTEIRO de "operacoes_matematicas"
print(multiplicar(5, 4)) #<--- importanto do módulo do "from operacoes_matematicas"
print(dividir(5, 4))     #<--- importanto do módulo do "from operacoes_matematicas"

print(str_utils.capitalizacao("hola"))
print(str_utils.inverter("hola"))
print(str_utils.contar("Marcos Pedrosa Quaresma"))