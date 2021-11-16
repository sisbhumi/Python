# Write a Python program to change a given string to a new string where the second and last chars have been exchanged.

s = input("Enter a string: ")
sec = s[1]
last = s[len(s)-1]

x = s[:1] + last + s[2:len(s)-1] + sec
print(x)