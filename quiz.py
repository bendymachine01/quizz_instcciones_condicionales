# Quiz instrucciones condicionales
"""
Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica,
determinar si pueden formar los lados de un triángulo.
"""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# Input
print("Ingrese los tres lados del triángulo:")
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# Processing
if a + b > c and a + c > b and b + c > a:
    print("\nLos lados pueden formar un triángulo.")
else:
    print("\nLos lados NO pueden formar un triángulo.")

print("\n--- Fin del programa ---")
