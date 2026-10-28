#Funcion para calcular el area de un triangulo o un cuadrado
calcular_area = {
      "triangulo",
      "cuadrado" 
}

#Definiciones de area
print("Vamos a hacer el calculo del area de una figura")
def area_triangulo(base, altura):
    return (base * altura) / 2
def area_cuadrado(lado):
    return lado ** 2

#Preguntamos que quiere calcular
figura = input("¿Qué área quieres calcular? (triangulo/cuadrado):")
#decidimos que queremos calcular
if figura == "triangulo":
    base = int(input("lado en cm"))
    altura = int(input("altura en cm"))
    respuesta = input("Estas preparado para hacer el calculo? (si/no): ")
    if respuesta == "si":
        resultado = area_triangulo(base, altura)
        print(f"El área del triángulo es: {resultado} cm²")
    else:
        print("Pues no te hago nada por listo")
elif figura == "cuadrado":
    lado = float(input("Introduce el lado en cm: "))
    respuesta = input("Estas listo para calcularlo? (si/no): ")
    if respuesta == "si":
            resultado = area_cuadrado(lado)
            print(f"El área del triángulo es: {resultado} cm²")
    else:
            print("Pues no te hago nada por listo")
else:
     print("A tanto no llego crack")
