# 62.Python program to display the sum of input (n) numbers using a list.

list1 = [11, 5, 17, 18, 23]
total = 0
for i in range(0, len(list1)):
    total = total + list1[i]

print("Sum of all elements in given list: ", total)