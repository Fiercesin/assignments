#Function to calculate the BMI index
def calculate(height, weight):
     bmi = weight/(height * height)
     return round(bmi,1)

Height = float(input("Enter your height in metres: "))
Weight = float(input("Enter your weight in Kilograms: "))

print("Your BMI index is:" , calculate(Height, Weight))

if calculate(Height, Weight) < 18.5:
    print("Underweight")

elif calculate(Height, Weight) >= 18.5 and calculate(Height, Weight) <= 24.9:
    print("Healthy weight")

elif calculate(Height, Weight) > 24.9 and calculate(Height, Weight)<= 29.9:
    print("Overweight")

else:
    print("Obese")

