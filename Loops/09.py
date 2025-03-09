# list uniqueness checker

# items = ['apple','banana','orange','apple','mango']
# for i in range(len(items)):
#     if(items.count(items[i])>1):
#         break
# print(items[i])

items = ['apple','banana','orange','apple','mango']
new = set()
for i in items:
    if i in new:
        print("duplicate ",i)
        break
    else:
        new.add(i)