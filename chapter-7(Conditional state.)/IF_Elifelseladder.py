a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
elif(a<0):    
    print("Invalid age entered")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("You are below the age of consent")    

print("End of program")