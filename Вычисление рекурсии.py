def factorial(n):
   # Базовый случай
   if n == 0:
       return 1

   # Рекурсивный случай
   else:
       return n * factorial(n — 1)

print(factorial(3))