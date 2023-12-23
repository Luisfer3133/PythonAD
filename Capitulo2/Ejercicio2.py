#Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
#del programa:

horas = input('Introduce las horas laboradas: ')
try:
    horas = int(horas)
    tarifa = input('Introduce la tarifa por hora: ')
    try:
        tarifa = int(tarifa)
        sueldo = horas * tarifa
        print(f'Sueldo: {sueldo}')
    except:
        print('Error, por favor introduce un numero.')
except:
    print('Error, por favor introduce un numero.')