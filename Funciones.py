''' 
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa. 
'''

'''1'''
def suma(a, b):
  return a + b
print(suma(5, 3))

'''2'''
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(6))

'''3'''
def es_primo(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True
print(es_primo(2))

'''4'''
def sumar_lista(lista):
  return sum(lista)
print(sumar_lista([8, 10, 3, 5, 9]))

'''5'''
def reversa(cadena):
  return cadena[::-1]
print(reversa("Raúl"))
