
s = {}  #it creates a dictionary
print(type(s))  #<class 'dict'>

s = {1, 2, 4}
print(type(s))  #<class 'set'>

#using set constructor
s = set((1,2,3,4,2)) #set from tuples
print( type(s), s)   #<class 'set'> {1, 2, 3, 4}

s = set( [1,2,7,5,4,2,1] ) #set from list
print( type(s), s) #<class 'set'> {1, 2, 4, 5, 7}

s = set("Hello!")  #set from string
print( type(s), s) #<class 'set'> {'e', '!', 'H', 'l', 'o'}

#sets are iterable
sset = {"apple", "banana", "cherry"}
for x in sset:
  print(x,end = " ")    #apple banana cherry

print("banana" in sset)  #True
print(len(sset))        #3

#adding and updating
sset.add("Kiwi")
print(sset)         #{'Kiwi', 'cherry', 'apple', 'banana'}
sset.update(s)
print(sset)         #{'apple', 'l', 'e', 'banana', 'cherry', 'Kiwi', 'o', 'H', '!'}
'''
#remove
#sset.remove('a')    #Gives error as a is not present in set
sset.discard('a')   #No error
sset.remove('apple')
print(print(sset))   #{'Kiwi', 'l', 'o', 'cherry', 'banana', 'e', 'H', '!'}

#pop
x = sset.pop()
print(x)  #Kiwi

#clear removes all set elements
s.clear()
print(s)  #set()

#del deletes the whole set
del s
print(s)      #NameError: name 's' is not defined
'''
#looping
for x in sset:
  print(x,end=" ")    #H o cherry e apple ! Kiwi banana l

#union

s1 = {1 , 2 , 3, 4}
s2 = {3 , 4 , 5 , 6}
print(s1.union(s2))     #{1, 2, 3, 4, 5, 6}
print(s1|s2)            #{1, 2, 3, 4, 5, 6}

#intersection
print(s1.intersection(s2)) #{3, 4}
print(s1&s2)               #{3, 4}

#difference
print(s1-s2)      #{1, 2}

#symmetric diff
print(s1^s2)      #{1, 2, 5, 6}




