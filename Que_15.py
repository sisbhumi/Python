#Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

def que15():
    x = int(input("Enter Units of electricity: "))
    cost = 0
    if x - 50 > 0:
        cost = 50*(.50)
        if x - 150 > 0:
            cost = cost + 75
            if x - 250 > 0:
                cost = cost + 120 + (x-250)*1.50
            else:
                cost = cost + (x-150)*1.20
        else :
            cost = cost + (x-50)*.75
    else:
        cost = x*(0.50)
    cost = cost + cost/5
    print("You have to Pay total amount of Rs.", cost)

que15()