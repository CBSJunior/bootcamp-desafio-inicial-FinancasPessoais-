import sqlite3
from datetime import datetime

def anotar_gasto():
    # Solicita informações ao usuário
    data_compra = input("Informe a data da compra (dd/mm): ")
    hora_compra = input("Informe a hora da compra (hh:mm): ")
    valor_compra = float(input("Informe o valor da compra: "))
    descricao = input("Informe uma breve descrição da compra: ")

    # Conecta (ou cria) o banco de dados
    conexao = sqlite3.connect("gastos.db")
    cursor = conexao.cursor()

    # Cria a tabela caso ela ainda não exista
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            data TEXT,
            hora TEXT,
            valor REAL,
            descricao TEXT
        )
    """)

    # Insere o registro no banco de dados
    cursor.execute("""
        INSERT INTO gastos (data, hora, valor, descricao)
        VALUES (?, ?, ?, ?)
    """, (data_compra, hora_compra, valor_compra, descricao))

    # Salva as alterações
    conexao.commit()

    # Encerra a conexão
    conexao.close()



anotar_gasto()

print("""
Neste 3º semestre, a turma está cursando a disciplina Desenvolvimento para
Ciência de Dados II, na qual estamos aprendendo programação em Python,
além da disciplina Estruturas para Ciência de Dados, que também envolve
o uso de Python e da ferramenta VSCode.

Durante o 1º bimestre da disciplina DCD II, aprendemos a realizar o
carregamento de bancos de dados no ambiente Python. Neste 2º bimestre,
que está se iniciando agora, passaremos a aprender como manipular esses
bancos de dados por meio da linguagem.

Dessa forma, a turma ainda não recebeu da universidade todos os
pré-requisitos necessários para executar o trabalho proposto.

Como por exemplo, nenhum professor já ensinou sobre "Testes Automatizados". 
O máximo que a turma aprendeu foi utilizar o Debug do Python para analisar o código.
""")