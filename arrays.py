"""
Date: 02-11-2023 2:09 PM
Author: Tahmid Chowdhury

Main Purpose: Working with Array Data Structures, single-dimensional & multi-dimensional
"""
from array import array
import numpy as np

print("\n1) This is creating an array in python:\n")
# This is creating an array in python
my_array = array("i",[1,2,3,4,5,6,7,8])
print(my_array)

print("\n2) Appending an element to the end of the array\n")
# Appending an element to the end of the array
my_array.append(9)
print(my_array)

print("\n3) Removing specific element from the array\n")
# Removing specific element from the array
my_array.remove(2)
print(my_array)

print("\n4) Iterating over the array\n")
# Iterating over the array
for i in range(len(my_array)):
    print(my_array[i])

print("\n5) Removing last element from the array\n")
# Removing last element from the array
my_array.pop()
print(my_array)

print("\n6) Adding items into array from a list\n")
# Adding items into array from a list
my_array.fromlist([9,10,11])
print(my_array)

print("\n7) Combining 2 arrays \n")
# Combining 2 arrays
my_another_array = array("i",[12,13])
my_array.extend(my_another_array)
print(my_array)

print("\n8) converting arrays to str \n")
# converting arrays to str
converted_str = my_array.tobytes()
print(converted_str)

print("\n9) converting bytes back to arrays \n")
# converting bytes back to arrays
empty_array = array("i")
empty_array.frombytes(converted_str)
print(empty_array)

print("\n10) reversing an array \n")
# reversing an array
empty_array.reverse()
print(empty_array)

print("\n10) slicing an array \n")
# slicing an array
sliced_array = empty_array[0:2]
print(sliced_array)



print("\n=============Two Dimensional Array================")

print("\n1) Creating 2dimentional array \n")
two_dimensional_array = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

print(two_dimensional_array)

print("\n2) inserting to the array as row\n")
new_added_two_dimen_array = np.insert(two_dimensional_array,0,[[3,6,9]],axis=0)
print(new_added_two_dimen_array)

print("\n3) inserting to the array as column\n")
new_added_two_dimen_array = np.insert(two_dimensional_array,0,[[3,6,9]],axis=1)
print(new_added_two_dimen_array)

print("\n4) appending to the array\n")
new_added_two_dimen_array = np.append(two_dimensional_array,[[3,6,9]],axis=0)
print(new_added_two_dimen_array)

print("\n5) accessing specific element from the 2dimentional array\n")
def access_two_dimensional_array(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("invalid Index")
    else:
        print(array[rowIndex,colIndex])

access_two_dimensional_array(new_added_two_dimen_array,0,2)

print("\n6) traversing 2dimentional array\n")
for r in range(len(new_added_two_dimen_array)):
    for c in range(len(new_added_two_dimen_array[0])):
        print(new_added_two_dimen_array[r][c])


print("\n7) search element from the 2dimentional array\n")
def search_two_dimensional_array(array,target):
    for r in range(len(array[0])):
        for c in range(len(new_added_two_dimen_array[0])):
            if array[r][c] == target:
                print("Succes Found at row,col",r,c)
                return
    print("Element not found")

search_two_dimensional_array(new_added_two_dimen_array,9)
