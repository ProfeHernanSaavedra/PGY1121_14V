import funciones as fn

op = 3
while op != 4:
  print("   MENU     ")
  print("*" * 10)
  print("1. Calcular IVA")
  print("2. Calcular Descuento")
  print("3. Calcular IMC")
  print("4. Salir")
  op = int(input("Ingrese su opción: "))

  if op == 1:
    precio = int(input("Ingrese precio del producto: "))
    iva = fn.calcularIva(precio)
    total = precio + iva
    print("El total a pagar es: $",total)
  if op == 2:
    precio = int(input("Ingrese precio del producto: "))
    desc = int(input("Ingrese descuento (0-100) %: "))
    fn.calculoDesc(precio,desc)
  if op == 3:
    peso = int(input("Ingrese su peso en Kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    fn.calculoIMC(peso,estatura)