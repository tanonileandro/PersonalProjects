# Prueba de la App
from POO.Leccion08.AppStorePc.Computadora import Computadora
from POO.Leccion08.AppStorePc.Monitor import Monitor
from POO.Leccion08.AppStorePc.Orden import Orden
from POO.Leccion08.AppStorePc.Raton import Raton
from POO.Leccion08.AppStorePc.Teclado import Teclado

# Objetos de Entrada
monitor = Monitor('LG', 27)
teclado = Teclado('Logitech', 'Bluetooth')
raton = Raton('Logitech', 'Bluetooth')
monitor1 = Monitor('Asus', 27)
teclado1 = Teclado('Redragon', 'Bluetooth')
raton1 = Raton('Redragon', 'Bluetooth')

# Objeto Computadora
computadora = Computadora('Gamer', monitor, teclado, raton)
computadora1 = Computadora('Diseño', monitor1, teclado1, raton1)
computadora2 = Computadora('Personal', monitor, teclado1, raton)

# Objeto Lista de computadoras
computadoras = [computadora, computadora1]
computadoras2 = [computadora2]

# Objeto Orden
orden = Orden(computadoras)
orden.agregarComputadora(computadora2)
orden1 = Orden(computadoras2)
print(orden)
print(orden1)
