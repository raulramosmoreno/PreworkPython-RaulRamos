'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos
'''

'''1'''
a = -10
if a > 0:
  print ("Es positivo")
else:
  print ("Es negativo")

'''2'''
n = 9
if n % 2 == 0:
  print("es par")
else:
  print("Es impar")
  
  '''3'''
b = 12
c = 11
d = 10
if b > c and d:
  print (b)
if c > b and d:
  print(c)
if d > c and d:
  print(d)