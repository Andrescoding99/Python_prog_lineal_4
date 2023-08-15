#Leer 5 valores
# Primero: ¿cual de lso 5 es el más alto?
# Segundo: ¿cual de lso 5 es el más bajo?

print("Lectura de su valores")

# Definicion de variables

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

# Captura de datos

num1 = float(input("\nIngresa el valor del primer número: "))
num2 = float(input("\nIngresa el valor del segundo número: "))
num3 = float(input("\nIngresa el valor del tercer número: "))
num4 = float(input("\nIngresa el valor del cuarto número: "))
num5 = float(input("\nIngresa el valor del quinto número: "))

#Calculo de operaciones 

# El mayor numero

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("\nEl mayor numero es ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El mayor numero es ", num2)
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El mayor numero es ", num3)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El mayor numero es ", num4)
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El mayor numero es ", num5)
else:
    if num1 == num2:
        print("Los numeros {} y {} son iguales" ).format(num1, num2)
    elif num1 == num2:
        print("Los numeros {} y {} son iguales" ).format(num1, num2)
    elif num1 == num3:
        print("Los numeros {} y {} son iguales" ).format(num1, num2)
    elif num1 == num4:
        print("Los numeros {} y {} son iguales" ).format(num1, num2)
    elif num1 == num5:
        print("Los numeros {} y {} son iguales" ).format(num1, num2)
    #Aqui harian falta otros 20 casos para validarlso todos con todos
# El menor numero

if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("\nEl menor numero es ", num1)
elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
    print("El menor numero es ", num2)
elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
    print("El menor numero es ", num3)
elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
    print("El menor numero es ", num4)
else:
    print("\nEl menor numero es " , num5)

