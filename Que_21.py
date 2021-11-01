#Print the following pattern
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

for i in range(1,6):
    print(i*"* ")
for i in range(6,10):
    print( (10-i)*"* ")