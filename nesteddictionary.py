s={
    101:{'name':'Harry','roll no': 101,'marks':90},
    102:{'name':'john','roll no': 102,'marks' : 95},
    103:{'name':'Ravi','roll no': 103,'marks': 86}
   }
for ch in s:
    print("For Roll no.",ch,"corresponding details are: ")
    for h in s[ch]:
        print(h, s[ch][h])