
number = '5' 

turn = 0

while turn < 3:
    
    if turn == 0:
        guess = input("Please Guess a number in between 0 and 9 : ")
    else:
        guess = input("Please guess again :  ")
    
    if guess == number :

        print('\nYOU WON :)')
        break

    elif guess != number:

        if turn < 2:
            print('OOPS! Try Again')
        elif turn == 2:
            print("\nSorry You Lost The Game :(")

    turn += 1
    