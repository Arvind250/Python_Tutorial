# my_list = [1,2,3,4]
# my_list.reverse()
# print(my_list)

# my_list = ['a','b','c','d','e']
# my_list[2:2] = ['2','3']
# print(my_list)
# print(type(my_list[0]))
# print(type(my_list[2]))

# my_list = [1,2,3,4]
# print(my_list)
# my_list.append(5)       #adding and removing item from the end
# print(my_list)
# my_list.pop()
# print(my_list)

# my_list.remove(1)
# print(my_list)             #adding and removing item at a index
# my_list.insert(0,1)
# print(my_list)

# my_list = [1,2,3,4,5]
# print(my_list)
# my_list_copy = my_list.copy()
# print(my_list_copy)
# my_list_copy[0] = 0
# print(my_list_copy)
# print(my_list)

# list1 = [1,2,3,4]
# list2 = list1.copy()
# print(list1 == list2)
# print(list1 is list2)

list1 = [1,2,3,4]
list2 = list1
print(list2)                #same reference is created in memory
print(list1 == list2)
print(list1 is list2)