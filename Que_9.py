#Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
a,b,c = [int(x) for x in input().split()]
sum = a+b+c
if a==b and sum/3 == a:
    print(4*sum)
else:
    print(sum)
