num = [6,5,9,12,56,10,15]
target = int(input("Enter the number to search: "))
low = 0
high = len(num)-1
found = False
while low <= high:
    mid = (low + high) // 2
    if num[mid]== target:
        print("element found: ", mid)
        found = True
        break
    elif target < num[mid]:
        high = mid - 1

    else:
        low= mid+1
if not found:
    print("Number not found in the list")        