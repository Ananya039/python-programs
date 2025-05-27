def Power(base,exponent):
    if exponent==0:
        return 1
    else:
        return base*Power(base,exponent-1)
base=int(input("Enter base: "))
exponent=int(input("Enter exponent: "))
result=Power(base,exponent)
print("Answer is: ",result)

