# Program to create a simple calculator using functions

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

num1=int(input("enter frist number:"))
num2=int(input("enter secound number:"))

print("select 1 opration:")
print(("[1] Addition(+)"))
print(("[2] Subtraction(-)"))
print(("[3] Multiplication(*)"))
print(("[4] Division(/)"))

choice = input("Enter your choice (1-4): ")

# Perform calculation
if choice == "1":
    print("Result:", add(num1, num2))

elif choice == "2":
    print("Result:", sub(num1, num2))

elif choice == "3":
    print("Result:", mul(num1, num2))

elif choice == "4":
    if num2 != 0:
        print("Result:", div(num1, num2))
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")
