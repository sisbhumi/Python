# A student will not be allowed to sit in exam if his/her attendance is less than 80%.
# Take following input from user:
#       Total Number of classes held
#       Total Number of classes attended.
#       And print percentage of class attended. Is student is allowed to sit in exam or not.
total = int(input("Enter the number of classes held."))
attended = int(input("Enter the number of classes you have attended."))
percent = round( attended*100 / total ,2 )

if percent < 80:
    print("You have attended just", percent,"percent of classes, so you cannot sit in exam.")
else : print("You have attended",percent,"percent of classes, so you can sit in exam.")