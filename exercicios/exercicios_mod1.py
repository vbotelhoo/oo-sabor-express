class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

restaurante_praca.nome  = 'Praça'
restaurante_praca.categoria = 'Gourmet'

print(f'Nome: {restaurante_praca.nome} Categoria: {restaurante_praca.categoria} Ativo: {restaurante_praca.ativo}')

restaurante_praca.categoria = 'Italiana'
print(f'Nome: {restaurante_praca.nome} Categoria: {restaurante_praca.categoria} Ativo: {restaurante_praca.ativo}')

nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)

if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está desativado')

categoria = Restaurante.categoria
print(categoria)

restaurante_praca.nome = 'Bistrô'
print(f'Nome: {restaurante_praca.nome} Categoria: {restaurante_praca.categoria} Ativo: {restaurante_praca.ativo}')

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print('É um fast-food')
else:
    print('Não é um fast-food')

restaurante_pizza.ativo = True
print(f'Ativo: {restaurante_pizza.ativo}')

print(f'Nome: {restaurante_praca.nome} Categoria: {restaurante_praca.categoria} Ativo: {restaurante_praca.ativo}')