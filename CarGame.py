
Help = 'Help'
start = 'Start'
stop = 'Stop'
Quit = 'Quit'
started = True
choice = ''


while True:
    
    print("\n------------Enter your choice-----------\n")

    choice = input()
    
    if choice.title() == Help :
        print( '''
Start -> To Start the car.
Stop -> To Stop the car.
Quit -To quit the game.
        ''')

    elif choice.title() == start:
        
        if started:
            print("CAR is already started.")
        else:    
            started = True
            print('The CAR is being started')

    elif choice.title() == stop: 
        
        if not started :
            print("CAR is already stopped")
        else:
            started = False
            print('The car is stopped')
    
    elif choice.title() == Quit :
        break
        
    else:
        print("OOPS! WRONG CHOICE.")