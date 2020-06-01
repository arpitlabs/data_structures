print("list")
# List
# A list in Python is a heterogeneous container for items.
# A list is mutable, so it is possible to reassign and delete individual items as well.
friends = ["a", "b", "c", 2, True, 4.5, [23, 54]]

# slicing operator ':'
print(friends[::2])

print()
print("tuple")
# Tuple
# A Tuple in Python is a heterogeneous container for items. Just like a list, but...
# they're fixed (immutable) unlike lists. They do not change.
tuple = ("A", "B") 
print(tuple)

# to add an element in a tuple
# create new tuple by adding two tuples, assign the addition to existing tuple
tuple = tuple + ("C",)
print(tuple)

# tuple packing
my_tuple = 1,2,3,4
print(my_tuple)

# tuple unpacking
a,b,c,d = my_tuple
print(a,b,c,d)

print()
print("set")
# set
# Unordered list with unique values
# No order/indexing, no duplicates, mutable.
team = {"AB", "BC", "CD", "BC"}
print(team)


print()
print("dictionary")
# dictionary
# Key-value pairs. Keys have to be unique. Mutable.
friends_age = {"Mike":34, "Jack":33}
print(friends_age["Mike"])