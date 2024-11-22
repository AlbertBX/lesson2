import math

num_a = float(input("Введите длину стороны квадрата: "))
if num_a<=0: print("Пожалуйста, вводите только положительные числа!")
else:
    def square(a):
      if num_a>=0: return math.ceil(a**2)
    print(f"Площадь квадрата: {square(num_a)}")
	
