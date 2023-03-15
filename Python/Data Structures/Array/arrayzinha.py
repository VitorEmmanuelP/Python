# As mentioned in the section above, arrays store only items that are of the same single data type
# https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/
# Be careful with the typecode 'i'
# Use like a list, Len, indenixg etc
import array as arr

numbers = arr.array('i',[10,20,30])


print(numbers)
# Len
print(len(numbers))
# INDEXING
print(numbers[0]) # gets the 1st element
print(numbers[1]) # gets the 2nd element
print(numbers[2]) # gets the 3rd element
print(numbers[-1]) #gets last item

# Search through
print(numbers.index(10))

# Loop
for number in numbers:
    print(number)

for value in range(len(numbers)):
    print(numbers[value])

# Slice
print(numbers[:2])  # first to second position

# Change value of an Item in an Array
numbers[0] = 40

# Add a New Value to an Array
numbers.append(40)
# Be aware that the new item you add needs to be the same data type as the rest of the items in the array.

# Entebd
numbers.extend([40,50,60])
#array('i', [10, 20, 30, 40, 50, 60])

# Insert ( Index, value)
numbers.insert(0,40)
#array('i', [40, 10, 20, 30])

# Remove a Value from an Array
numbers.remove(10)

# pop passa o index
numbers.pop(0)

