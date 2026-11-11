# Program to find the largest of three numbers

# Take input from the user for three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Condition to check which number is largest among three

if num1 > num2 and num1 > num3:
    print(num1, "is largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is largest number")
else:
    print(num3, "is largest number")