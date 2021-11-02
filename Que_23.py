#Program to check whether a given number is a palindrome or not

num = int(input("Enter a number: "))
n = num
rev = 0

while num != 0:
    rev = rev*10 + num%10
    num = num//10

if n == rev:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")