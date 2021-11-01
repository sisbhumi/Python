# Calculate income tax for the given income by adhering to the below rules
# Taxable Income        Rate (in %)
# First Rs.10,0000         0
# Next Rs. 10,0000       10
# The remaining           20
net_income = int(input("Enter your net income: "))
tax = 0
if net_income > 200000  :
    tax = (net_income-200000)*2 / 10
    tax = tax + 10000
elif net_income > 100000:
    tax = (net_income - 100000) / 10

print("Tax you have to pay: ",   tax)
