from POO.Leccion08.AppStorePc.Monitor import Monitor
from POO.Leccion08.AppStorePc.Raton import Raton
from POO.Leccion08.AppStorePc.Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nommbre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'''
                {self._nombre}: {self._idComputadora}
                    Monitor: {self._monitor}
                    Teclado: {self._teclado}
                    Raton: {self._raton}
        '''
if __name__ == '__main__':

    monitor = Monitor('LG', 27)
    teclado = Teclado('Logitech', 'Bluetooth')
    raton = Raton('Logitech', 'Bluetooth')
    computadora = Computadora('Gamer', monitor, teclado, raton)
    print(computadora)