#Ejercicio 3: Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular el salario bruto.
horas = input('Introduce las horas laboradas: ')
horas = int(horas)
tarifa = input('¿Cual es la tarifa por hora? ')
tarifa = int(tarifa)
salario = horas*tarifa
print(salario)