"""
1	Display float number with 2 decimal places using print()
2	Takes two integer numbers and  return their product.
3	Write a Python program to get the volume of a sphere with radius 10.
4	Accept two numbers from the user and multiply them together.
5	Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
6	Write a Python program to calculate the length of a string
7	Write a Python program to parse a string to Float & Integer
"""
def que_1():
    x  = 12.3345
    print(round(x,2))
#output: 12.33

def que_2(a , b):
    return a*b
#Output: 20

def que_3(radius):
    volume = 4/3*3.14*radius**3
    print(round(volume,2))
#Output: 4186.67

def que_4():
    a = int( input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(a*b)
#Output: Enter 1st number: 5
#        Enter 2nd number: 8
#        40

def que_5():
    a = input("Enter a number: ")
    res = int(a) + int(a+a) + int(a+a+a)
    print(res)
#Output: Enter a number: 4
#        492

def que_6():
    s = "Hello friends! Chai pi loo."
    print("Length of string '"+s+"' is ",len(s))
#Output: Length of string 'Hello friends! Chai pi loo.' is  27

def que_7():
    a = "65841"
    b = "123.45"
    c = int(a)
    d = float(b)
    print( type(a), type(b), type(c), type(d) )
#Output:  <class 'str'> <class 'str'> <class 'int'> <class 'float'>


que_1()
product = que_2(4,5)
print(product)
que_3(10)
que_4()
que_5()
que_6()
que_7()