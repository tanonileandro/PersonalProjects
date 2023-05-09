from POO.Leccion08.AppStorePc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(marca, tipoEntrada)


    def __str__(self):
        return f'ID: {self._idTeclado} | Marca: {self.marca} | Tipo de Entrada: {self.tipoEntrada}'


if __name__ == '__main__':
    teclado = Teclado('Asus', 'Wireless')
    teclado2 = Teclado('Logitech', 'Bluetooth')
    print(teclado)
    print(teclado2)
