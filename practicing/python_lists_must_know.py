# LISTS
# Lists are mutable data types in Python

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
print(lst[-5]) # Output: x

# Slicing
print(lst[:2]) # Output: ['x', 'b']

# Adding, removing and inserting elements into a list
lst.append(5)
print(lst) # Output: ['x', 'b', 'c', 'd', 'e', 5]

remove = lst.pop()
print(remove, lst) # Output: 5 ['x', 'b', 'c', 'd', 'e'], This line of code prints the removed item which is assigned to 'remove' variable and the current list.

remove_1 = lst.pop(2)
print(remove_1, lst) # Output: c ['x', 'b', 'd', 'e']

lst.remove("b")
print(lst) # Output: ['x', 'd', 'e'], If we have two 'b's in the list then it only removes the first instance

lst.insert(2, 10000) # first argument is for the specified index and second argument is the value we want to add to the list
print(lst) # Output: ['x', 'd', 10000, 'e']

lst.append([1, 2]) # This adds the list as an own element
print(lst) # Output: ['x', 'd', 'e', [1, 2]]

lst.extend([1, 2]) # In this way you can add this list as individual data
print(lst) # Output: ['x', 'd', 'e', [1, 2], 1, 2]

# Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][1]) # Output: 4

nested_list_1 = [
    [1, 2],
    [3, [4]],
]
print(nested_list_1[1][1][0]) # Output: 4

# List Slicing
# [start:stop:step]
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst_1[:]) # This crates a hole copy of the list

print(lst_1[1:]) # Output: [2, 3, 4, 5, 6, 7, 8]

print(lst_1[1:6]) # Output: [2, 3, 4, 5, 6]

print(lst_1[1:6:2]) # Output: [2, 4, 6]

print(lst_1[:-1]) # Output: [1, 2, 3, 4, 5, 6, 7]

print(lst_1[-1:]) # Output: [8]

print(lst_1[::-1]) # Reverses the order of the list

lst_1[2:4] = [1000, 1000]
print(lst_1) # Output: [1, 2, 1000, 1000, 5, 6, 7, 8]

# Useful List Methods 
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 3]

contains = 2 in lst_2
print(contains) # Output: True

index = lst_2.index(3)
print(index) # Output: 2

count = lst_2.count(3)
print(count) # Output: 2

print(lst_2.sort()) # Output: None, This is because the .sort() function does not return anything it just sort the list.
print(lst_2) # Output: [1, 2, 3, 3, 4, 5, 6, 7, 8]

print(lst_2.sort(reverse=True))
print(lst_2) # Output: [8, 7, 6, 5, 4, 3, 3, 2, 1]

print(lst_2.reverse())
print(lst_2) # Output: [1, 2, 3, 3, 4, 5, 6, 7, 8]

print(sorted(lst_2)) # This does not effect the original list
print(lst_2) # Output: [1, 2, 3, 3, 4, 5, 6, 7, 8]

print(reversed(lst_2))
print(lst_2) # Output: [8, 7, 6, 5, 4, 3, 3, 2, 1]

# Copying and modyfing a list
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
copy_of_list = original_list[:]
copy_of_list[0] = 'a'
print(f"Original List: {original_list}, Copy of List: {copy_of_list}")

