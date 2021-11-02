#   Program to find whether a given number is a strong number or not.
#       e.g. n=145
#       1!+4!+5!==145

num = int(input("Enter a number: "))
n = num
fact = 0
while n != 0:
    x = n%10
    f = 1
    while x != 0:
        f = f*x
        x -= 1
    n = n//10
    fact += f

if fact == num:
    print("Yes")
else:
    print("NO")
