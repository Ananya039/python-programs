def add (x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x/y
print("Select operator: + , - , * , /")
choice = input("Enter choice: ")
n1 = int(input("Enter 1st operator: "))
n2 = int(input("Enter 2nd operator: "))
if choice == "+":
    print("Result", add(n1,n2))
elif choice == "-":
    print("Result", subtract(n1,n2))
elif choice == "*":
    print("Result", multiply(n1,n2))
elif choice == "/":
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result", divide(n1,n2))  
else:
    print("Invalid operator")          

