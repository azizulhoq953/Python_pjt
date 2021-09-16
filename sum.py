
#from typing import Text


numberOfDigit=0
numberOfLetter=0
numberOfWord=0

 text= input("Enter Any Number & Digit & Word:");
 
 for x in text:
     x=x.lower();
     if x>= 'a' and x <='z':
         
         numberOfLetter=numberOfLetter +1 
    elif x >= '0' and x <='9':
        numberOfDigit=numberOfDigit +1
        
    
         
    elif x == ' ':
       numberOfWord=numberOfWord +1
       
       
        print(numberOfDigit)
        print(numberOfLetter)
        print(numberOfWord)
 


















#n=input("Enter Any Numbers:");

#list=n.split()

#sum=0               #user input and sum

#for num in list:
 #   t=int(num)
  #  sum=sum+t
    
  #  print(sum)
