#Program to find whether a given number is a perfect number or not.
n = int(input("Enter a number."))
sum = 1

i = 2
while i * i <= n:
    if n % i == 0:
        sum = sum + i + n / i
    i += 1
if sum == n:
    print("It is  a perfect number.")
else: print("Not a perfect number. ")