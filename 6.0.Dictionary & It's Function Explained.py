# Making a dicitionary?
dic1 = {'duck':'quack','cow':'mooh','tiger':'roar'}
print(dic1['cow'])

                                     # Accesing Elements
# get vs [] for retrieving elements
my_dic = {'name':'Jack','age':'26'}

# Output : Jack
print(my_dic['name'])

# Output : 26
print(my_dic['age'])

                                      # Changing & Adding elements
#update value
#my_dic['age']=27

# Output : {'name': 'Jack', 'age': 27}
print(my_dic)

# add item
my_dic['address'] = 'Downtown'

# Output : {'name': 'Jack', 'age': 27, 'address': 'Downtown'}
print(my_dic)

                                       # Removing elements
# Removing element from a dicitionary

squraes = {1:1,2:4,3:9,4:16,5:25}
# removing a particular item
print(squraes.pop(4))
# removing a particular item using del function
del squraes[1]
# Output : {2: 4, 3: 9, 5: 25}
print(squraes)
#remove an arbitary item
print(squraes.popitem())
# Output : {2: 4, 3: 9}
print(squraes)
# remove all items
squraes.clear()

print(squraes)