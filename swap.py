# swap two numbers with using remp variable or with temp variable..
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print('Old value of num1 is {0} and num2 is {1}'.format(num1,num2))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print('New values of num1 is {0} and num2 is {1}'.format(num1,num2))