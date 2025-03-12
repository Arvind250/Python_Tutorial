#print all the elements of the list with its index provided using recursion
def print_item(list,i):
    if i == len(list):
        return
    else:
        print(list[i])
        print_item(list,i+1)
print_item([1,2,3,'a','b'],1)