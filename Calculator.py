from math import * 
from decimal import Decimal
while  True:
 num1 = Decimal( input(" Enter the frist number :"))

 operator = input ( " Enter the asrithmatic operation (+, -, *, /, %, ^, <, >, @):") 

 num2 = Decimal ( input (" Enter the seconde number :"))

 if operator == "+" : 
    print ("\n The resolet is :", num1 + num2,"\n")
 elif operator ==  "*" :
    print ("\n The resolet is :", num1 * num2,"\n")
 elif operator == "-" :
    print ("\n The resolet is : ", num1 - num2,"\n")
 elif operator == "/" : 
    if num2 == 0 :
        print ("Error: Cannot dividenby zero.") 
    else :
     print("\n The resolet is : ", num1 / num2,"\n")
 elif operator == "%" : 
    print ("\n The resolet is : " , num1 % num2,"\n")
 elif operator ==">" :    
     print ("\n The resolet is :" , max(num1 , num2))
 elif operator == "<" :
     print ("\n The resolet is :" , min(num1 , num2))
 elif operator == "^" :
    print ("\n The resolet is :" , pow(num1 , num2))
 elif operator == "@" : 
    print ("\n The resolet is :" , sqrt(num1))
 else : 
    print ("Invalid operator.")  
   
