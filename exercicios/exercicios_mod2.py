
class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    def listar_carro():
            for carro in Carro.carros:
                 print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro_celta = Carro('Celta', 'Prata', '2007')

Carro.listar_carro()

class Restaurante:
     restaurantes = []
     def __init__(self, nome, categoria):
            self.nome = nome
            self.categoria = categoria
            self.ativo = False
            Restaurante.restaurantes.append(self)

     def __str__(self):
           return f'{self.nome} | {self.categoria}'
     
hanoi=Restaurante('Hanoi', 'Japones')
print(hanoi)

class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')    