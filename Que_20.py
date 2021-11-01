# Find the sum of the series 3 +33 + 333 + 3333 + .. n terms
n = int(input("Enter number of terms: "))
sum = 0
series = 0
while n:
    series = series*10 + 3
    sum = sum + series
    n-=1
print(sum)