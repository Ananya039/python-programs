num = int(input("Enter a numbrer: "))
if( num>=1):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print(num, "is not a prime no.")
            break
        else:
            print(num, "is prime no.")
else:
    print(num, "is not a prime no.")            