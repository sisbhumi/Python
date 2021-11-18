#51. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()).
# Write code to test this function with different inputs.

def min_max(a,b,c):

    m = min(a,b,c)
    mx = max(a,b,c)

    if( m<a<min ):
        return a
    if( m<b<mx ):
        return b
    if( m<c<mx ):
        return c

a = int(input("Enter three numbers: "))
b = int(input())
c = int(input())

print( min_max(a,b,c) )