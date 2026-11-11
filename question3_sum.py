# Program to calculate sum of numbers from 1 to n.

# Input last number
n = int(input("Enter positive number: "))

# Total starts from 0
total = 0

# Loop for counting from 1 to n
for i in range(1, n+1):
    total += i

print("Sum of numbers from 1 to", n, "is:", total)