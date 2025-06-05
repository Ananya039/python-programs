# break is used to come ouut of the loop when encountered .
# it instruct the program to exit the loop now.

for i in range(100):
    if(i==34):
        break        # Exit the loop right now

    print(i)


for i in range(100):
    if(i==34):
        continue      # Skip the iteration right now
    
    print(i)    