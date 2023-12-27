#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
#1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

horas = input('Introduce tus horas laboradas: ')
horas = float(horas) #Los convierto en float ya que la tarifa se multiplicara por un float (1.5), asi que los resultados del salario seran en float.
tarifa = input('Introduce la traifa por hora: ')
tarifa = float(tarifa)
if horas>40:
    tarifa = tarifa * 1.5
else:
    pass
salario = horas*tarifa
print(f'Salario: {salario}')
