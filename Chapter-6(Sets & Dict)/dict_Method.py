marks = {
    "Riya" : 90,
    "Shila" : 85,
    "Hina" : 95,
}
print(marks.items()) # Returns a view object that displays a list of a dictionary's key-value tuple pairs


print(marks.keys()) 

print(marks.values())

marks.update({"Riya": 95 , "pihu": 100})
  # Updates the value for the key "Riya" to 95
print(marks)

print(marks.get("Riya3"))  # Prints None if the key "Riya3" does not exist, instead of raising an error
print(marks["Riya3"])
      
      
''' get()	Get value of a key (safe)	d.get('key', default)
keys()	All keys	d.keys()
values()	All values	d.values()
items()	All (key, value) pairs	d.items()
update()	Merge/update dictionary	d.update({'k': v})
pop()	Remove key, return value	d.pop('key')
popitem()	Remove last item	d.popitem()
clear()	Remove all items	d.clear()
copy()	Shallow copy	d.copy()
setdefault()	Get value if exists; else insert default value	d.setdefault('k', v)
     '''