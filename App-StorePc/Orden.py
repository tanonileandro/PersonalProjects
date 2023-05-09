class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadora(self):
        return self._computadoras

    @computadora.setter
    def computadora(self, computadoras):
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''
        Orden: {self._idOrden} 
            Computadora: {computadoras_str}
        '''
