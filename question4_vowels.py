# Program to count vowels in a string 

text=input("enter your name: ")

count=0

for ch in text:
    if ch.lower() in "aeiou":
        count+=1

print("Total number of vowels:", count)