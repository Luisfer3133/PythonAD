#Ejercicio 5: ¿Qué mostrará en pantalla el siguiente programa Python?

respuesta = input('''¿Qué mostrará en pantalla el siguiente programa Python? 
def fred():
    print("Zap")
                 
def jane():
    print("ABC")
 
jane()
fred()
jane()
                 
a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC
e) Zap Zap Zap
                  
''')

if respuesta == 'd':
    print('Tu respuesta es correcta')
else:
    print('Tu respuesta es incorrecta')