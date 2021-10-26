#11 - To check whether a number is divisible by 8 and 12 or not.
#12 - To check whether a given number is even or odd.
def que11(num):
    if num % 8 == 0 and num % 12 == 0:
        return True
    else:
        return False

def que12(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if que11(num):
    print("Given Number is divisible by 8 and 12.")
else:
    print("Given number is not diisible by 8 and 12.")

if que12(num):
    print("The given number is even.")
else:
    print("The given number is odd.")
