#Program to check whether a given number is an Armstrong number or not.
num = int(input("Enter a number: "))
n = num
armstg = 0

while n != 0:
    armstg = armstg + pow(n%10,3)
    n = n//10

if armstg == num:
    print("Yes")
else:
    print("No")
