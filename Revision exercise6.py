# Christopher pullen
#21/10/14
#revision exercise 6

print (" this program will show a conversion table from pounds to kilograms")

pounds = 2.2
for count in range (1,21):
    result=count/pounds
    print (" {0:<2} / {1:>2} = {2:.1f}" .format (count, pounds, result)) 
