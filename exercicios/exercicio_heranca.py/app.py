from veiculos.carro import Carro
from veiculos.moto import Moto

carro_celta = Carro('GM', 'Celta', False, 2)
moto_cg = Moto('Honda', 'CG-250', True, 'Casual')

def main():
    print(carro_celta)
    print(moto_cg)

if __name__ == '__main__':
    main()