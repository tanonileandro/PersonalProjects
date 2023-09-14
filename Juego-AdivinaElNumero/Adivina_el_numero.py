from random import randint

print('-' * 50)
print('Bienvenidos a \"Adivina el número\"'.center(50, ' '))
print('-' * 50)

secret_number = randint(1, 100)
tries = 0
number = 0
name = input('Dime tu nombre: ')

print(f'\nHola {name}!. \nTienes 8 intentos para adivinar el número secreto que he elegido entre 1 y 100.\n')


while tries < 8:
    try:
        number = int(input(f'\n=> Intento número {tries + 1}: '))
        while number < 1 or number > 100:
            print('\nValor ingresado incorrecto!\n')
            number = int(input(f'=> Por favor, ingrese nuevamente un número entre 1-100: '))

    except ValueError:
        print('Por favor ingrese un valor valido...')
        continue

    if number == secret_number:
        print(f'¡Felicitaciones {name}! Adivinaste el número en {tries + 1} intentos')
        break

    elif number < secret_number:
        print("El número secreto es mayor.")

    else:
        print("El número secreto es menor.")

    tries += 1

if number != secret_number:
    print(f'\n¡Lo siento! Te has quedado sin intentos. El número secreto era {secret_number}.')