#Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-y￾media para las horas extras, y crea una función llamada calculo_salario
#que reciba dos parámetros (horas y tarifa).

horas = input('Introduce tus horas laboradas: ')
horas = float(horas) #Los convierto en float ya que la tarifa se multiplicara por un float (1.5), asi que los resultados del salario seran en float.
tarifa = input('Introduce la traifa por hora: ')
tarifa = float(tarifa)

def calculo_salario(horas, tarifa):
    if horas>40:
        tarifa = tarifa * 1.5
    else:
        pass
    
    salario = horas*tarifa

    return f'Salario: {salario}'

print(calculo_salario(horas, tarifa))
