mensaje ="hola mundo"
nombre=""
ecuacion = 0
numero = 0

print(mensaje)

nombre = input('''\nBienbenido al mundo de la programacion

Para continuar, ingresa tu nombre
               ''')

print(f"Bienvenido {nombre}")

numero = int(input("ingrese un valor para 'X' en la ecuacion '(X^2+3X+1)/4' "))
ecuacion = (numero**2+3*numero+1)/4
print(ecuacion)

nombre = input("ingrese su nombre: ")
rut = input("ingrese su rut: ")
correo = input("ingrese su correo: ")
telefono = int(input("ingrese su telefono: "))

print(f'''
NOMBRE:	  {nombre}	
RUT:	  {rut}		
CORREO:	  {correo}	
TELEFONO: {telefono}      
      ''')
