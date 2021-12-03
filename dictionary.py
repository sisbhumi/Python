
my_dict={}

my_dict

my_dict={ 1: 'Apple' , 2: 'Banana'}
my_dict

my_dict={'name':'apple', 2: [1,2,3] }
my_dict

#using dict() function
my_dict=dict({1:'apple',2:'banana'})
my_dict

#my_dict=dict([1:'apple',2:'banana'])  #this line will give error 
my_dict=dict([(1, 'apple'), (2,'banana')])
my_dict

print(my_dict[1])

my_dict=dict([('name','apple'),('type','fruit')])
print(my_dict['name'])

my_dict['price']=300
my_dict

#pop(key) , popitem() , clear() , del
sq={1:1, 2:4, 3:9, 4:16, 5:25}
sq

print(sq.pop(4))

sq

print(sq.popitem())

sq

sq.clear()
sq

sq={1:1, 2:4, 3:9, 4:16, 5:25}
del sq
sq

sq={1:1, 2:4, 3:9, 4:16, 5:25}
print(sq.items())