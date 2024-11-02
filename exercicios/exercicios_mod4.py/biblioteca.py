#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from livros import Livro

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_escolhido = 2020
livros_disponiveis = Livro.verificar_disponibilidade(ano_escolhido)
print(f'Livros disponiveis em {ano_escolhido}:')
for livro in livros_disponiveis:
    print(livro)