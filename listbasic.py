name = []
n = int(input("Enter number of entries you want"))

#for taking values of list as input
for i in range( 0 , n ):
    na = int(input('Enter number: '))
    name.append(na)
#for printing all elements of list
for i in name :
    print(i)
#for adding all values of list
sum = 0
for i in range ( 0 , n ):
    sum += name[i]
print(f'sum = {sum}')

#for finding largest number in list    
larg = 0
for i in range(0,n):
    if name[i] > larg:
        larg = name[i]
print( f'largest number = {larg}' )