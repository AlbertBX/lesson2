def month_to_season(n):
     if 1<=n<=2 or n==12:
        print ("Зима")
     if 3<=n<=5:
        print ("Весна")
     if 6<=n<=8:
        print ("Лето")
     if 9<=n<=11:
        print ("Осень") 
     if n<=00 or 13<=n:
        print ("Пожалуйста, введите любое положительное целое число месяца от 1 до 12.")      
try:
    n= int(input("Введите число месяца года: "))
    month_to_season(n)
except ValueError:
    print ("Пожалуйста, введите любое целое число месяца от 1 до 12.")

