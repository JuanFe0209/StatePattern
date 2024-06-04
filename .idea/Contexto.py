from OffEstate import OffState
class Contexto:
    def __init__(self):
        self.estado_actual = OffState()

    def set_estado(self, estado):
        self.estado_actual = estado

    def usarPower(self):
        self.estado_actual.usarPower(self)

    def usarHome(self):
        self.estado_actual.usarHome(self)
