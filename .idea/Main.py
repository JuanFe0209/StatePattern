from Contexto import Contexto

if __name__ == "__main__":
    dispositivo = Contexto()

    # Estado inicial: EstadoOff
    dispositivo.usarPower()  # Transición a EstadoBloqueado
    dispositivo.usarHome()   # Transición a EstadoListo
    dispositivo.usarHome()   # Transición a contexto del sistema
    dispositivo.usarPower()  # Transición a EstadoOff
