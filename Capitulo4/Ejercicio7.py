#Ejercicio 7: Reescribe el programa de calificaciones del capítulo ante￾rior usando una función llamada calcula_calificacion, que reciba una
#puntuación como parámetro y devuelva una calificación como cadena

calf = input('Introduzca su puntuación: ')
try:
    calf = float(calf)
    def calcula_calificacion(calificacion):  
            if calificacion>=0.9 and calificacion<=1.0:
                return 'Sobresaliente'
            elif calificacion>=0.8 and calificacion<0.9:
                return 'Notable'
            elif calificacion>=0.7 and calificacion<0.8:
                return 'Bien'
            elif calificacion>=0.6 and calificacion<0.7:
                return 'Suficiente'
            elif calificacion<=0.5 and calificacion>=0.0:
                return 'Insuficiente'
            else:
                 print('Dame un numero valido para tu calificación.')
        
    print(calcula_calificacion(calf))

except:
    print('Dame un numero valido para tu calificación.')

menor = None
print('Antes: ', menor)
for n in [4,8,3,56,45]:
		if menor is None or n<menor:
				menor = n
		print('Bucle: ', n, menor)
print('Menor: ', menor)