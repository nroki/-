import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        num = int(input("������� ������������� ����� �����: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("�� ����� ������������ ��������. ����������, ������� ������������� ����� �����.")

result = factorial(num)
if result > math.factorial(100):
    print(f"��������� {num} ������� ����� ��� ������������ ����������, ����������� ���������� math.")
else:
    print(f"��������� {num} ����� {result}")