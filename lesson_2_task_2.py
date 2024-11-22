def is_year_leap(year):
    if year % 4==0:
        print ("True")
    else:
        print ("False")
try:
    year = int(input("Введите целое число года: "))
    is_year_leap(year)
except ValueError:
    print("Пожалуйста, введите целое число.")

   
