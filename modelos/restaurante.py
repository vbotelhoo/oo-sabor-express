from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return self._nome
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if nota >= 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return f'Não avaliado'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_das_notas / qtd_notas, 1)
        return media
    
    def  adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                msg_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(msg_prato)
            else:
                msg_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(msg_bebida)