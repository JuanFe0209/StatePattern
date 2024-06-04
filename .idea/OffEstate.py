from Estado import Estado
class OffState(Estado):
    def usarPower(self, contexto):
        print("Transición de Off a Locked")
        contexto.set_estado(LockedState())

    def usarHome(self, contexto):
        print("El sistema está apagado.")

class LockedState(Estado):
    def usarPower(self, contexto):
        print("Transición de Locked a Off")
        contexto.set_estado(OffState())

    def usarHome(self, contexto):
        print("Transición de Locked a Ready")
        contexto.set_estado(ReadyState())

class ReadyState(Estado):
    def usarPower(self, contexto):
        print("Transición de Ready a Off")
        contexto.set_estado(OffState())

    def usarHome(self, contexto):
        print("El sistema ya está listo.")
