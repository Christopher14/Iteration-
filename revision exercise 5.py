#Christopher pullen
#21.10.14
#revision exercise 5

print ("please enter a series of numbers and enter a negative value when you wish for the average to be created")

value=0
count=0
number =0
while number >=0:
    number=int(input("please enter a number"))
    if number >=0:
        value= value +number
        count +=1
    # else:
          #average = value/count
          # print ("Your average is {0} " .format (average ))
    # average doesn't have to be with in the while loop can just be a process after it :)
average = value/count
print ("Your average is {0} " .format (average))

        
