#validate_mastervisa.py
#Liu Feng Yuan 5c23 16
#Date created 19/1/2013
#Check whether a card number of visa or master is valid


import re

cardnum=input("Please enter your card number:")


def mastervisa(cardnumber):

    if len(cardnumber) == 13 or len(cardnumber) == 16:
        if cardnumber[0] == '4':
            return "It is Visa"
        elif cardnumber[0] == '5':
            return "It is Master"
        else:
            return "Invalid digit"
    else:
        #neither visa nor master
        return ("Incorrect number of digit")


    
def validcardnum(cardnumber):
    #find all the digits in cardnum 
    cardnumber = re.findall('[0-9]+',cardnumber)
    cardnumber=''.join(cardnumber)
    #check whether card is master and visa+elinminate some invalid number
    cardtype=mastervisa(cardnumber)
    total=0
    
    if cardtype=="It is Visa" or cardtype=="It is Master":
        for i in range(0,len(cardnumber)):
            #add odd numbers
            if i%2!=0:
                total=total+int(cardnumber[i])
            #add all even number    
            else:
                x=int(cardnumber[i])*2
                if x>9:
                    #if x is 2 digit,add the total of its first and second digit 
                    x=int(str(x)[0])+int(str(x)[1])
                total=total+x
        if total%10==0:
            return "It is a valid number"
        else:
            return "It is a invalid number"
                

    else:
        return cardtype

print (validcardnum(cardnum))
