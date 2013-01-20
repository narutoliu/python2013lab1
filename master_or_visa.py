#master_or_visa
#Liu Feng Yuan 5c23 16
#Date created 19/1/2013
#Check whether a card number is visa or master

import re

cardnum=input("Please enter your card number:")


def mastervisa(a):
    #find all the digits in cardnum 
    cardnumber = re.findall('[0-9]+',a)
    cardnumber=''.join(cardnumber)
    if len(cardnumber) == 13 or len(cardnumber) == 16:
        if cardnumber[0] == '4':
            return "It is Visa"
        elif cardnumber[0] == '5':
            return "It is Master"
        else:
            return "Invalid digit"
    else:
        #neither visa nor master
        return "Incorrect number of digit"


    
print (mastervisa(cardnum))
