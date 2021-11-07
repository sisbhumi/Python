# Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xbc ayz'
s  = 'xyz,abc'
l = s.split(',')
a = l[1]+l[0]
print(a)