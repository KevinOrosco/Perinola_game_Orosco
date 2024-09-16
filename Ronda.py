from Jugador import Jugador

class Ronda:
    def __init__(self):
        self.jugadores = []
    
    def __repr__(self):
        return f"{self.jugadores}"
    
    def agregarJugador(self):
        jugador = Jugador()
        if jugador.fichas <= 0:
            raise ValueError("El jugador debe tener al menos 1 ficha para ser agregado.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        for jugador in self.jugadores:
            if jugador.fichas == 0:
                self.jugadores.pop(jugador) 


    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if jugador.fichas > 0]

    def jugadorEnTurno(self):
        if not self.jugadores:
            return None
        return self.jugadores[0]

    def pasarTurno(self):
        if self.jugadores:
            jugador = self.jugadores.pop(0)
            self.jugadores.append(jugador)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1