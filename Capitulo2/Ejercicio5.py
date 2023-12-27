#Ejercicio 5: Escribe un programa que le pida al usuario una temper￾atura en grados Celsius, la convierta a grados Fahrenheit e imprima
#por pantalla la temperatura convertida.

grados_celcius = input('Dame una temperatura en grados celcius: ')
grados_celcius = float(grados_celcius)
grados_f = (grados_celcius*9)/5 + 32
print(f'Serian {grados_f} grados Fahrenheit')