# texto_variado = 'Palabra 123 +-* #$&'
# print(type(texto_variado))

# #Podemos utilizar comillas triples para que el texto se muestre tal cual
# print(''' 
# Funcionamiento de \
# programa: (opciones)
# -1 Para acceder a opciones
# -2 para salir                  
# ''')

#subscripthig e indexado

texto = 'Python'

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])
#No se puede acceder a una posición que no existe

# letra = texto[0]
# print(letra)

# letra = 'p'
# print(letra)

# texto_compuesto = letra + texto[1] #concatenación
# print(texto_compuesto)

#Slicing o substrinhing

# texto = 'Python'
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[2:])

print('{} + {} = {}'.format(2, 3, 2+3))
print('{}+{} ={}'.format('Hola', 'mundo', 'Hola Mundo'))
print('{:3f}+{:4f}={}'.format(2,3,2+3))
print('{1}+{0}= {2}'.format(2,3,2+3))
