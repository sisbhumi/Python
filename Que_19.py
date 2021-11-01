#Program to find the digital product of a given number
#   ex: n=43   Digital product ----->4*3=12

num = int(input("Enter a number: "))
prod = 1
while num != 0 :
    prod = prod * (num%10)
    num = num//10
print(prod)