print("Hello from list.py")

# list - store list of items
#  createed by putting items inside square brackets []

list = [] # empty list
numbers_list = [1, 2, 3, 4] # list of integers
colors_list = ['red', 'blue', 'green']
mixed_list = [1, 5, 'orange' , 4.7]

print(colors_list)

my_list = ['Python', 'Java', [1, 2, 3], 'Amit']

# access elements from a list

numbers = [1, 2, 3, 4, 5, 6]

print(numbers)

print(numbers[2]) # index position 3, index start from 0 to above

# print(numbers[7]) # def hello(name, msg = "How are you")
print(numbers[-1]) # last elements of the list
print(numbers[-2]) # second last elements od the list

print(numbers[2:5]) # third to sixth elements
print(numbers[2:]) # third to last element
print(numbers[:-2]) # beginning to third
print(numbers[:]) # beginning to end

# list are mutable - item can be changed

my_colors = ['red', 'green', 'blue', 'yellow', 'brown']

print(my_colors)
my_colors[2] = 'pink'

print(my_colors)

my_colors[1:3] = ['orange', 'purple']  #second and 3rd item of list get change

print(my_colors)

# add item to a list

numbers = [1, 2, 3, 4]
print(numbers)
numbers.append(5)
print(numbers)
numbers.extend([6, 7, 8])
print(numbers)

#  combine lists using +
print(numbers + [9, 10])

#  repeat items using *

print(numbers * 3)

#  insert item in the list at a desired location insert()
numbers.insert(2, 2.5)
print(numbers)

#  delete item - del

del numbers[2] # delete the 3rd item

print(numbers)

del numbers[2:4] # delete multiple items

print(numbers)

del numbers # delete the entire list

# print(numbers)

print('---------------------------------------')

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.remove(1)   # remove item 1, it is not depends on index number

print(numbers)

print('---------------------------------------')

numbers.pop(2)  # remove (poped) the item from index number 2 (index start from 0)

print(numbers)

numbers.pop() # poped or delete the last item

print(numbers)
print('---------------------------------------')
numbers.clear()   # to clear the list
print('---------------------------------------')
print(numbers)

#  copy list = 

list1 = [1, 2, 3]
list2 = list1

print(list2)

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

# loop thriugh a list
fruits = ['apple', 'banana', 'grapes', 'strawberry']

for item in fruits:

  print(item)
print('---------------------------------------')
# check item in list

print('apple' in fruits)
print('orange' in fruits)
print('---------------------------------------')

my_list = [1, 2, 3, [4.4, 7.7, 8.8], 'one', 'two'] # nested list (list in the list) [[[]]]

print(my_list[3][2])

print(my_list[3][0])







