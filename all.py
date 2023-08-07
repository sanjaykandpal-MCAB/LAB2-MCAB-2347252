#   Sort the dictionaries in ascending order based on the Key of the dictionary.
def sort_dict_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    return sorted_dict


# Example dictionary
example_dict = {'apple': 3, 'banana': 1, 'orange': 5, 'grape': 2}

# Sort the dictionary in ascending order based on keys
sorted_dict = sort_dict_by_key(example_dict)

# Print the sorted dictionary
print("Sorted Dictionary (Ascending Order):", sorted_dict)

# Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary

def calculate_sum_of_values(dictionary):
    listNum = list(dictionary.values())
    sum = 0
    for x in listNum:
     sum += x
    return sum


# Example dictionary with numeric values
numeric_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Calculate the sum of all the values in the dictionary
sum_of_values = calculate_sum_of_values(numeric_dict)

# Print the sum of all the values
print("Sum of all the values in the dictionary:", sum_of_values)

# Write a Python code to demonstrate the sorting in descending order of values with lambda function.
def sort_dict_by_value_desc(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


# Example dictionary with numeric values
numeric_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Sort the dictionary in descending order based on values
sorted_dict = sort_dict_by_value_desc(numeric_dict)

# Print the sorted dictionary
print("Sorted Dictionary (Descending Order of Values):", sorted_dict)

# Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods )

thisList = ["blog","comment","post","user"]
print(thisList)

thisList.append("Dislikes") # append element at end position 
print(thisList)


thisList.insert(2,"Sharing") # insert at specific position
print(thisList)

secondList = ["Authentication","Authorization"]

thisList.extend(secondList) # this method add the specified element to the end current list


sets = {"blog1","blog2","blog3","blog4","blog5"}
thisList.extend(sets) #adding sets to list using extend method
print(thisList)

dictionary = {"img": "url","id": "value2"} #adding dictionary to list using extend method
thisList.extend(dictionary)
print(thisList) 

tuple = ("comment",True) #adding tuple to list using extend method
thisList.extend(tuple)

print(thisList)


print(thisList[-1]) #this list will print from end of list

print(thisList[2:5]) # this will print 2,3,4 element from list

print(thisList[:4]) # this will print 0,1,2,3 but not 4

#thisList.sort()
#print(thisList) # this will sort the list (not supported for string and boolean)

copyList = thisList.copy() # copy the entire list to another variable
print(copyList)

# Create a list with numeric and perform the following operations.
# ·       Write a program to swap the first and last elements in a list.

list = [1,2,3,4,5]

swapFirst = list[0]
swapLast = list[len(list)-1]
temp = 0 

temp = swapFirst 
swapFirst = swapLast
swapLast = temp

list[0] = swapFirst
list[len(list)-1] = swapLast

print(list)

# Create a list with numeric and perform the following operations.
# Write a program to find the sum of the digits in a list.

list = [1,2,3,4]
sum = 0
for x in  list:
   sum += x

print(sum)

# Create a list with numeric and perform the following operations.
# Write a program to find the smallest element in a list

list =[10,454,42,48,1,2,3,4,5]

list.sort()

print(list[0])

