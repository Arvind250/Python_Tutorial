# my_dict = {"name":"John","age":21,"place":"U.S"}
# print(my_dict)
# my_dict["age"]=22
# print(my_dict)

# my_dict = {"name":"John","age":21,"place":"U.S"}
# for key,value in my_dict.items():
#     print( key , value)

# my_dict = {"name":"John","age":21,"place":"U.S"}
# my_dict["salary"] = 12000
# print(my_dict)
# print(len(my_dict))

# my_dict = {"names":{"name1":"John","name2":"Alice","name3":"Bob"},"age":21,"place":"U.S"}
# print(my_dict)
# print(len(my_dict))
# my_dict["names"]["name1"]="Cena"
# print(my_dict)


# my_dict = {"names":{"name1":"John","name2":"Alice","name3":"Bob"},"age":21,"place":"U.S"}
# print(list(my_dict.keys()))
# print(type(list(my_dict.values())))       
# new = list(my_dict.values())
# print(type(new),len(new),new)

# my_dict = {"names":{"name1":"John","name2":"Alice","name3":"Bob"},"age":21,"place":"U.S"}
# new= tuple(my_dict.items())     #class here is dict_item
# old = list(my_dict.items())
# print(old,new)
# old[0]=('hello','John')         #interchanging the datatypes
# print(old)
# print(my_dict)
# new_dict = dict(old)
# print(new_dict)

# my_dict = {"names":{"name1":"John","name2":"Alice","name3":"Bob"},"age":21,"place":"U.S"}
# # print(my_dict['place1'])                         #this returns error 
# print(my_dict.get('place2'))                       #this returns no error (none)

# my_dict = {"name":"John","age":21,"place":"U.S"}
# my_dict.update({'salary':20000})
# print(my_dict)

# my_dict = {                                         #multiple value and be added to a key in form of lists or tuple
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture","list of fact and figures"]
# }
# print(my_dict["table"][0])


#PRACTICE QUESTION  
# my_dict = dict()
# subject = input("Enter your subject1 name : ")
# marks = int(input("Enter your marks1 : "))
# my_dict.update({subject:marks})
# subject = input("Enter your subject2 name : ")
# marks = int(input("Enter your marks2 : "))
# my_dict.update({subject:marks})
# subject = input("Enter your subject3 name : ")
# marks = int(input("Enter your marks3 : "))
# my_dict.update({subject:marks})
# print(my_dict)