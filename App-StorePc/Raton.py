from POO.Leccion08.AppStorePc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'ID: {self._idRaton} | Marca: {self.marca} | Tipo de Entrada: {self.tipoEntrada}'


if __name__ == '__main__':
    raton = Raton('Logitech', 'USB')
    print(raton)
