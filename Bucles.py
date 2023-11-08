'''
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''

'''1'''
for a in range(11):
  if a >0:
    print(a)

'''2'''
b = 1
while b <= 20:
  b= b+1
  if b % 2 == 0:
    print(b)
    
'''3'''
c = 0
for d in range(101):
  c = c+d
print (c)

  