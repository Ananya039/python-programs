num = [41,67,45,98,78,45,34]
unique_numbers = list(set(num))
unique_numbers.sort(reverse=True)
if len(unique_numbers)>= 2:
    print("Second largest number is:",unique_numbers[1])
else:
    print("List does not have second largest number")    
