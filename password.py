import string
name=input("enter your password") #name is the variable used to get password to be generated
f=len(name) # f used to fix the length of the password
if f<15:
    print("use minimum 15 letters")
else:
    count=0 #initializing all the variables related to fixing the count of lower, upper,digit,special characters
    count1=0
    count2=0
    count3=0
    n=range(0,10)
    l=list(string.ascii_uppercase) #initialize the uppercase letters from A - Z
    l1=list(string.ascii_lowercase) #initialize the lowercase letters from a-z
    l3=list(n) #initialize the list of numbers from 0 to 9
    for i in name:
        if i in l:
            count=count+1
            if(count<=2):
                pass
            else:
                print("crossed the upper case limit")
                break
        elif i in l1:
            count1=count1+1
            if(count1<=5):
                pass
            else:
                print("crossed the lower case limit")
                break
        elif i in str(l3):
                count2=count2+1
                if(count2<=5):
                    pass
                else:
                    print("crossed the number limit")
                    break
        else:
            count3=count3+1
            if(count3<=3):
                pass
            else:
                print("crossed special character limit")
                break
    else:
        print("over")
                
                
     
            




        
       
        
   
    
        
 
