# 47)Write a Python program to compute sum of digits of a given string.
str1 = "OPPP-116M25A"
sum_digit = 0
for x in str1:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z
print(sum_digit)
