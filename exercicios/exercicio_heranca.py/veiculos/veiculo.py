class Veiculo:
    def __init__(self, marca, modelo, estado):
        self.marca = marca
        self.modelo = modelo
        self._estado = False

    def __str__(self):
        status = 'On' if self._estado else 'Off'
        return f'MARCA : {self.marca} | MODELO : {self.modelo} | ESTADO : {status}'