#Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
#puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
#está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

puntacion = input('Dame una puntuacion entre 0.0 y 1.0: ')
try:
    puntacion = float(puntacion)

    if puntacion<0.0 or puntacion>1.0:
        print('Error, el valor que ingresaste esta fuera del rango aceptable.')
    elif puntacion>= 0.9:
        print('sobresaliente')
    elif puntacion>= 0.8:
        print('Notable')
    elif puntacion >= 0.7:
        print('Bien')
    elif puntacion >= 0.6:
        print('SUficiente')
    elif puntacion < 0.6:
        print('Insuficiente')

except:
    print('Puntuacion incorrecta.')

entero = int('35.5')
print(entero)