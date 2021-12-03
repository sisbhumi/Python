

my_tuple=()
my_tuple #or print(my_tuple)

my_tuple=(1,2,3)
my_tuple

my_tuple=(1,"hello",3.14)
my_tuple

#nested tuple
my_tuple=('house',[1,4,5],(3.14,5.5,60.5))
my_tuple

my_tuple=4,5.4,"dog"
my_tuple

#unpacking
a,b,c=my_tuple
print(a," ",b," ",c)

a,b,c=4,3.14,'hello'
print(a," ",b," ",c)

my_tuple=("HEllo")
print(type(my_tuple))

my_tuple=("HEllo",)
print(type(my_tuple))

my_tuple=("c","s","i","t","b","r","a","n","c","h")
print(my_tuple[0])
# print(my_tuple[2.0]) will give as we cannot give index as float value

#my_tuple[0]='d' and del my_tuple[2] wil give error as tuples are immutable
t1=(5,3.14,"hello")
t2=([1,2,6],"rat",(7.1,5.58,8.05))
t3=t1+t2
t3

my_tuple=('house',[1,4,5],(7,3,9))
print(my_tuple[1][0])
print(my_tuple[2][2])
print(my_tuple[-1])
print(my_tuple[-1][-1])
print(my_tuple[:])
print(my_tuple[:-2])
print(my_tuple[-2:-2])

print((1,2,3)+(4,5,6))

print(('repeat',)*5)
print((1)*5)
print((1,)*6)

my_tuple=(4,5,7)
del my_tuple
type(my_tuple)

my_tuple=('a','p','p','l','e')
my_tuple.count('p')

print(my_tuple.index('a'))
print(my_tuple.index('l'))
print(my_tuple.index('p'))

print('a' in my_tuple)
print('b' in my_tuple)

for i in ('CSIT','Acropolis'):
  print("Hello ",i)

a=(1,2,3)
for i in a:
  print(i**2)

# a.sort() will not work in tuple as tuple are immutable
b=sorted (a)
b