import math

def square(a):
    return math.ceil(a**2)

num_a = float(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(num_a)}")
if num_a<=0: print("Пожалуйста, вводите только положительные числа!")
	