'''
print("Hola mundo")
nom = input("Ingrese su nombre: ")
print("su nombre es: ",nom)
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Ud es mayor de edad")
else:
    print("Ud es un niño")
'''

def sumar(a,b):
    suma = a + b
    print("la suma es: ", suma)
# fin funcion

def sumar2(a,b):
    suma = a + b
    return suma
# fin funcion


num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

sumar(num1,num2)
suma2 = sumar2(num1,num2)
print("la suma 2 es: ",suma2)
