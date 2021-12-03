#Python program to delete an element from a list by index which is given by the user.
l1=list(input("Enter the list ").split(" , "))
k=int(input("Enter the index from which the element to be deleted "))
l1.pop(k)
print(l1)