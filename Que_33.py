#Print following pattern:
#A
#BB
#CCC
#DDDD
#EEEEE
#FFFFFF
#GGGGGGG
#FFFFFFFF

n = 1
for i in range(65,73):
    print(chr(i) * n)
    n+=1