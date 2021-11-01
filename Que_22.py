#Program to reverse a given Number.    ex: n=123   Reversed no is 321
num = int(input("Enter a number: "))
rev = 0
while num != 0:
    rev = (rev*10) + (num%10)
    num = num//10

print(rev)