#christopher pullen
#revision exercise 4
#17/10/2014

print (" please enter a number when asked")

valid= False
while not valid:
    number = int(input("enter a number between 10 and 20"))
    if 10<=number<=20:
        print ("number entered is valid!")
        valid = True
    else:
        print ("the number entered is not valid please try again:")
    

    
