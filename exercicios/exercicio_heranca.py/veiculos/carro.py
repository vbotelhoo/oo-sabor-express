from veiculos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, estado, portas):
        super().__init__(marca, modelo, estado)
        self.portas = portas
    
    def __str__(self):
        status = 'On' if self._estado else 'Off'
        return f'MARCA : {self.marca} | MODELO : {self.modelo} | PORTAS : {self.portas} | ESTADO : {status}'