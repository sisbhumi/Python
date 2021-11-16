#Program to find whether a given number is a prime number or not.
from math import sqrt
n = int(input())
x = True
if (n <= 1):
    x = False

for i in range(2, int(sqrt(n)) + 1):
    if (n % i == 0):
        x = False

if x:
    print("Prime Number.")
else: print("Non Prime.")