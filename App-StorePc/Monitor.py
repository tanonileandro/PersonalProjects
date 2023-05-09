class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, dimension):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._dimension = dimension

    @property
    def idMonitor(self):
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        self._dimension = dimension

    def __str__(self):
        return f'ID: {self._idMonitor} | Marca: {self._marca} | Tamaño: {self._dimension}\"'


if __name__ == '__main__':
    monitor = Monitor('LG', 27)
    print(monitor)
