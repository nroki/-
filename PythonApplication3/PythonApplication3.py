import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        num = int(input("Введите положительное целое число: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("Вы ввели недопустимое значение. Пожалуйста, введите положительное целое число.")

result = factorial(num)
if result > math.factorial(100):
    print(f"Факториал {num} слишком велик для стандартного вычисления, используйте библиотеку math.")
else:
    print(f"Факториал {num} равен {result}")