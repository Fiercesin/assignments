bill = int(input("Enter the total bill amount? "))
tip = int(input("Enter  the percentage of your tip either 10%, 12%, 15%: "))
people = int(input("How many people are splitting the bill: "))

total = ((bill/100) * tip) + bill
individual_bill = round(total/people, 2)
print("Total amount to be paid by each person is: " , individual_bill)


