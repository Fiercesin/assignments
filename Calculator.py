''' Adrian Baraka
    sct211-0022/2022 '''

#Prompt for user input
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Prpmpt for operation to be performed
print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
operation = int(input("Enter the number of the operation that is to be performed: "))

print ("The answer is: ")
if operation == 1:
     print (num1 + num2)

elif operation == 2:
    print (num1 - num2)

elif operation == 3:
    print (num1 * num2)

elif operation == 4:
    print (num1 / num2)

else:
    "Invalid operation"



