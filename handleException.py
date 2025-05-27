try:
    num= int(input("Enter a number: "))
    res = 10/0
    print("Result is", res)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
