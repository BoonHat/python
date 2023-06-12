#can be repeateable cuz it use index
mylist = ['apple','banana','cherry']
print(mylist)

#to read the list on the front
print(mylist[1])
#to read the list on the back
print(mylist[-1])

#to read the range of index
print(mylist[1:2])

#read it from the start
print(mylist[:2])
#read until the end
print(mylist[1:])

#check if item is there
if 'apple' in mylist:
    print('apple')