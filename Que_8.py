#Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
def sum(a,b):
    return a+b
def prod(a,b):
    return a*b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if sum(a+b)>100:
    print("Product is",prod(a,b))
else: print("Sum is",sum(a+b))