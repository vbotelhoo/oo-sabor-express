from veiculos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, estado, tipo):
        super().__init__(marca, modelo, estado)
        self.tipo = tipo

    def __str__(self):
        status = 'On' if self._estado else 'Off'
        return f'MARCA : {self.marca} | MODELO : {self.modelo} | TIPO : {self.tipo} | ESTADO : {status}'
