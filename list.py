'''
Las listas son un tipo de dato que nos permite almacenar varios valores en una misma variable.
Para definir una lista, se utilizan corchetes [] y se separan los valores por comas.
'''

list 
camiseta = ["rojo", "L", 100, 10]
print(camiseta)

nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre + "!")

# Ejemplo de un bucle while en Python



contador = 0

while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1
 
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")
 

for i in range(5):  # 0 a 4
        print("Número:", i)

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Primer elemento

persona = {"nombre": "Carlos", "edad": 25, "ciudad": "México"}
print(persona["nombre"])  # Acceder a un valor

def saludar(nombre):
    return "Hola, " + nombre + "!"

print(saludar("Carlos"))

texto = "Hola, mundo!"
longitud = len(texto)
print("La longitud del string es:", longitud)