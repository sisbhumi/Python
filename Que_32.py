#Print  following pattern:
#1
#12
#123
#1234
#12345
#123456
#1234567
#12345678
#123456789

for i in range(1,11):
    for j in range(1,i):
        print(j,end="")
    print()
