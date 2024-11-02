from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Vitor', 2)
restaurante_praca.receber_avaliacao('Victoria', 5)
restaurante_praca.receber_avaliacao('Thiago', 4)

def main():
        Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()