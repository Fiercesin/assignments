def leap_year(year):
    if(year%4 == 0):
        return True
    else:
        return False


Year = int(input("Enter your year of birth: "))
if leap_year(Year) == True:
    print(Year, "was a leap year.")
else:
    print(Year, "was not a leap year.")
