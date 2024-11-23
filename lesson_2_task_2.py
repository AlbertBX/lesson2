def is_year_leap(year):
    if year % 4==0:
        return True
    else:
        return False
        
try:
    year = int(input("Введите целое число года: "))
    result=is_year_leap(year)
    print(f"год {year}: {result}")
except ValueError:
    print("Пожалуйста, введите целое число!")

   
