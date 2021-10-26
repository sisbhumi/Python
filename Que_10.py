#A shop will give discount of 50% if the cost of purchased quantity is more than 10000.
# Ask user for quantity suppose, one unit will cost 100.
#Judge and print total cost for user.

cost = int(input("Enter cost fof 1 Unit: "))
quantity = int(input("Please Enter quantity of material purchased: "))
if cost*quantity>10000:
    amt = 50/100*(cost*quantity)
    print("Congratulations!\nApko milta h 50% discount.")
else:
    amt = cost*quantity

print("Total amount you have to pay is", amt,"\nPlease visit again!")