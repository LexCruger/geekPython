
from  math import factorial

e = int(input("Введите конечное число: "))

def fact(n):
  for i in range(1,n + 1):
    yield(factorial(i))

for el in fact(e):
  print(el)