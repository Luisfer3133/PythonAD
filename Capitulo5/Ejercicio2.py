contador = 0
total = 0
lista = []
mayor = None
menor = None
while True:
    try:
        numero = input('Introduzca un numero: ')
        if numero == 'fin':
            break
        else:
            numero = float(numero)
            contador = contador + 1
            lista.append(numero)
            total = total + numero
        
    except:
            print('Entrada invalida')
            continue
print(total, contador,total/contador)
for n in lista:
    if mayor is None or n>mayor:
        mayor = n
print('Mayor: ', mayor)
for n in lista:
     if menor is None or n<menor:
          menor = n
print('Menor: ', menor)