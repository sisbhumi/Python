# Write a Python program to remove the characters which have even index values of a given string.
s = input("Enter a string.\n")
temp = ''
for i in range(len(s)):
    if i % 2 == 0:
        temp = temp + s[i]
print(temp)