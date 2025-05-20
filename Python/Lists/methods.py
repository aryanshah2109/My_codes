import string
l = [1, 3, 5, 2, 4]


print("\nList is ", l)

# 1. Length of list
print("\n1. Length of list")
print("Length of list 1 is ", len(l))  # returns length of list

# 2. Max and Min of list
print("\n2. Max and Min of list")
print("Maximum of list 1 is ", max(l))  # returns maximum of list
print("Minimum of list 1 is ", min(l))  # returns minimum of list

# 3. Append in list
print("\n3. Append in list")
l.append(9)  # adds an element to the list
print("List l after appending 9 is ", l)

# 4. Sort the list
print("\n4. Sort the list")
l.sort()  # sorts the list in ascending order
print("Sorted list l in ascending order is ", l)

l.sort(reverse=True)  # sorts the list in descending order
print("Sorted list l in descending order is ", l)

l2 = [1, 3, 5, 1, 2, 4, 1, 3]

print("\nList l2 is ", l2)

# 5. Reverse the list
print("\n5. Reverse the list")
l2.reverse()  # reverses original list
print("Reverse of list l2 is ", l2)

# Now, after reversal l2 = [3, 1, 4, 2, 1, 5, 3, 1]

# 6. Remove an element from list
print("\n6. Remove an element from list")
l2.remove(1)  # removes first occurrence of 1 from list
print("List l2 after removing 1 is ", l2)

# 7. Pop an element from list
print("\n7. Pop an element from list")
l2.pop(1)  # removes element at index 1 from list
print("List l2 after popping element at index 1 is ", l2)

# 8. Index
print("\n8. Index")
print("Index of first occurrence of 3 in list l2 is ", l2.index(3))  # returns index of first occurrence of item written in list

# 9. Count
print("\n9. Count")
print("Count of 1 in list l2 is ", l2.count(1))  # returns the count of the specified item

# 10. Copy
print("\n10. Copy")
l3 = l2.copy()  # creates a shallow copy of the list
l3[0] = 0
print("Copy of list l2 is ", l3)
print("Original list: ",l2)

# 11. Insert
print("\n11. Insert")
l2.insert(3, 1000)  # inserts an item at the specified position
print("List l2 after inserting 1000 at index 3 is ", l2)

# 12. Concatenation
print("\n12. Concatenation")
k = l + l2  # concatenates two lists
print("Concatenated list k is ", k)

# 13. Extend
print("\n13. Extend")
l3.extend(l2)  # extends the list by appending elements from another list
print("List l3 after extending with l2 is ", l3)

# 14. Clear
print("\n14. Clear")
l3.clear()  # clears the list
print("List l3 after clearing is ", l3)


l4 = list(string.ascii_letters)
l5 = list(string.digits)
print(l4,l5)


