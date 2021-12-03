

my_list=[]
my_list

my_list=[1,2,3]
my_list

my_list=[1,"hello", 3.4]
my_list

my_list=['c', 's', 'i' ,'t', 'a', 'c', 'r', 'o']
my_list[0]

my_list=['c', 's', 'i' ,'t', 'a', 'c', 'r', 'o', [2,0,1,3]]
my_list[-1][1]

my_list[2:5]

my_list[-1][1]= 9 #list are mutable
my_list

my_list= [2,3,4,6,7,8,8]

my_list[1:4]= [4,4,4]
my_list

my_list.append(10)
my_list

my_list.extend([9,11,14])
my_list

print(my_list  + [11,12,13])

print(["hello"] *5])

print(["hello"] *5)

my_list.insert(1, 90)
my_list

my_list.append([10])
my_list

my_list.append(my_list)
my_list

odd=[1]
my_list.append(odd)
my_list

my_list[-1][0]

my_list[-2][0]

my_list[-2]

my_list= [1,2,2,3,4,5,6,7,8,9]
my_list.remove(3)
my_list

my_list.pop(1)

print(my_list.pop(1))

my_list.clear()
my_list

my_list=[1,2,3,4]
my_list.pop()

my_list.index(3)

my_list=[1,2,2,2,2,2,3,4,5,6]
my_list.count(2)

del my_list

my_list

l=[9,8,7,6,5,4,3,2,1]
l.sort()
l

l.reverse()
l

#LIST COMPREHENSION - CONSIST OF EXPRESSION FOLLOWED BY FOR LOOP INSIDE SQUARE BRACKETS]
pow=[ x**2 for x in range(10)]
pow

pow=[]
for x in range(10):
    pow.append(x**2)
pow

pow=[ 2**x for x in range(10) if x>5]
pow

even=[x for x in range (51) if x%2==0]
even

odd=[x for x in range (51) if x%2!=0]
odd

# NESTED FOR LOOP
L= [x+y for x in ['python', 'C'] for y in ['language', 'programming']] 
print ("hello" in L)

for i in [0,1,2,3,4]:
    print(i)