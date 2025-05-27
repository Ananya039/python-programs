num = [5,6,9,55,23,12]
target = int(input("Enter the number to search: "))
found = False
for i in range(len(num)):
    if(num[i]== target):
        print("Element found:", i)
        found = True
        break
if not found:
    print("Element not found in the list")