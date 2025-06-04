   # it is immutable data type in nature.
# Tuple is a collection of ordered elements, which can be of different data types.
# It is similar to a list, but it is immutable, meaning that once created, its elements cannot be changed.
# Example of a tuple

a = (4,6,5,3)
print(type(a))  

b = () # Empty tuple

c = (1,)  # Single element tuple, note the comma

d = (1,45,65,34,True, "Riya","shila")

a[1] = 5  # This will raise an error because tuples are immutable



