#Program to find whether a given number is a unique number.
# For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers

n = int(input())
l = []
while n!=0:
    l.append(n%10)
    n = n//10
s = set(l)

if len(s) == len(l):
    print("Unique Number.")
else:
    print("Not Unique.")
