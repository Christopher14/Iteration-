#Christopher pullen
#10.10.2014
# Ascii exercise

print (" whould you like to convert ascii to to text or text to ascii?")

request = int(input("1.ascii to text or 2.text to ascii"))

if request == 1:
    ascii_code = int(input("please enter an ascii code"))
    ascii_text = chr(ascii_code)
    print ("{0}" .format (ascii_text))
elif request ==2:
    text = ord(input("please enter the text you with to convert into ascii"))
    print ("{0}" .format (text))
else:
    print ("please enter a valid request 1")
    
                     
