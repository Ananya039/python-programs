n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
lcm =max(n1,n2)
while True:
    if(lcm % n1 == 0 and lcm % n2 == 0):
        print(lcm)
        break
    lcm+=1
