#  13 - Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
#       Calculate percentage and grade according to following:
#       Percentage >= 90% : Grade A
#       Percentage >= 80% : Grade B
#       Percentage >= 70% : Grade C
#       Percentage >= 60% : Grade D
#       Percentage >= 40% : Grade E
#       Percentage < 40% :  Grade F

# noinspection PyPep8Naming
def que13():
    phy = int(input("Enter Marks Out of 100.\nPhysics: "))
    chem = int(input("Chemistry: "))
    bio = int(input("Biology: "))
    math = int(input("Mathematics: "))
    com = int(input("Computer: "))

    total = phy + chem + bio + math + com
    Percentage = total/5

    if   Percentage >= 90 : print("Grade A")
    elif Percentage >= 80 : print("Grade B")
    elif Percentage >= 70 : print("Grade C")
    elif Percentage >= 60 : print("Grade D")
    elif Percentage >= 40 : print("Grade E")
    elif Percentage <  40 : print("Grade F")

#  14 - Take input of age of 3 people by user and determine oldest and youngest among them.

def que14():
    a,b,c = [ int(x) for x in input("Enter age of three persons: ").split() ]
    print("The Oldest person is of age:",max(a,b,c))
    print("The Youngest person is of age:", min(a, b, c))


que13()
que14()