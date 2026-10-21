# Módulos em Python

Repositório de estudos sobre o uso de módulos em Python. Os exemplos exploram recursos da biblioteca padrão, a criação e importação de módulos próprios e a construção de uma interface gráfica simples.

## Organização

- [`aulas/`](./aulas): exemplos práticos organizados por módulo.
- [`organizar/`](./organizar): materiais relacionados à organização do projeto.

## Conteúdo das aulas

| Script | Tópicos estudados |
| --- | --- |
| [`01_modulo_os.py`](./aulas/01_modulo_os.py) | Módulo `os`: diretório atual, listagem de arquivos e execução de comandos do Windows. O script consulta informações do sistema, limpa o terminal e cancela um desligamento agendado; também define funções para agendar desligamentos, que só têm efeito quando chamadas. |
| [`02_modulo_math.py`](./aulas/02_modulo_math.py) | Módulo `math`: constantes matemáticas, arredondamento para cima/baixo, fatorial, potência, raiz quadrada, MDC e logaritmo. |
| [`03_modulo_estatisticas.py`](./aulas/03_modulo_estatisticas.py) | Módulo `statistics`: média, mediana, moda e desvio padrão de conjuntos de dados. |
| [`04_modulo_re.py`](./aulas/04_modulo_re.py) | Expressões regulares com `re`: busca de padrões, índices de correspondência, caracteres especiais, faixas de caracteres e verificações de início/fim de texto. |
| [`05_modulo_hashlib.py`](./aulas/05_modulo_hashlib.py) | Módulo `hashlib`: consulta de algoritmos disponíveis e geração de hashes SHA-256 e MD5. Hashes não são criptografia reversível; MD5 é apresentado apenas como exemplo legado, não como opção segura para aplicações novas. |
| [`06_modulo_colecoes.py`](./aulas/06_modulo_colecoes.py) | `collections`: contagem de elementos com `Counter`, registros com `namedtuple` e filas de duas extremidades com `deque`; ordenação de pares com `operator.itemgetter`. |
| [`07_modulo_aleatorio_random.py`](./aulas/07_modulo_aleatorio_random.py) | Módulo `random`: escolha e amostragem de elementos, geração de inteiros aleatórios e um jogo interativo de adivinhação. |
| [`08_modulo_tkinter.py`](./aulas/08_modulo_tkinter.py) | Interface gráfica com `tkinter`: janela, `Frame`, rótulos, campo de texto, botão e atualização de conteúdo por callback. |
| [`main.py`](./aulas/main.py) | Programa principal que importa módulos próprios integralmente ou funções específicas e demonstra suas chamadas. |
| [`operacoes_matematicas.py`](./aulas/operacoes_matematicas.py) | Módulo próprio com funções de soma, subtração, multiplicação e divisão, incluindo validação de divisão por zero. |
| [`str_utils.py`](./aulas/str_utils.py) | Módulo próprio com funções para capitalizar, inverter e contar caracteres de uma string. |

## Execução

Execute os comandos a partir da pasta raiz do repositório, com Python 3:

```bash
python aulas/main.py
```

Para executar uma aula individual, por exemplo:

```bash
python aulas/02_modulo_math.py
```

Alguns exemplos solicitam entrada pelo terminal. A aula de Tkinter abre uma janela gráfica. A aula de `os` executa comandos do sistema operacional; revise o script antes de executá-lo. Os exemplos usam módulos da biblioteca padrão do Python, sem dependências externas.
