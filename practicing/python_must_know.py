# LISTS

# Indexing
lst = ["a", "b", "c", "d", "e"]
# index:0    1    2    3    4
# index:-5  -4   -3   -2   -1

print(lst[4]) # Output: e
print(lst[len(lst) - 1]) # Output: e, more verbose method. A liitle bit more difficult to read.

# Changing value by indexing
lst[0] = "x"
print(lst) # Output: ['x', 'b', 'c', 'd', 'e']

# Negative Indexing
print(lst[-5]) # Output: a

# Slicing
print(lst[:2]) # Output: ['a', 'b']

# Adding, removing and inserting elements into a list
lst.append(5)
print(lst) # Output: ['x', 'b', 'c', 'd', 'e', 5]

remove = lst.pop()
print(remove, lst) # Output: ['x', 'b', 'c', 'd', 'e'], This line of code prints the removed item which is assigned to 'remove' variable and the current list.

remove_1 = lst.pop(2)
print(remove_1, lst) # Output: ['x', 'b', 'd', 'e', 5]

lst.remove("b")
print(lst) # Output: ['x', 'd', 'e', 5], If we have two 'b's in the list then it only removes the first instance





