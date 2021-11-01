#Program to find digital sum of a given Number
#   ex: n=123  Digital sum----->1+2+3=6
num = int(input("Enter a number: "))
sum = 0
while num != 0 :
    sum = sum + num%10
    num = num//10
print(sum)