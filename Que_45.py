# 45)Write a Python program to find the maximum occurring character in a given string.
str1 = "Chacha Chodhari"
ASCII_SIZE = 256
ctr = [0] * ASCII_SIZE
max = -1
ch = ''
for i in str1:
    ctr[ord(i)] += 1;

for i in str1:
    if max < ctr[ord(i)]:
        max = ctr[ord(i)]
        ch = i
print(ch)

