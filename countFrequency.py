data = [10,45,34,23,10,55,55]
freq = {}
for items in data:
    if items in freq:
        freq[items] += 1
    else:
        freq[items] =1
print("frequency of elements: ")
for key in freq:
    print(key, ":", freq[key])        


