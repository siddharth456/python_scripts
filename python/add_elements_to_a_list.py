# add elements to an empty list

testlist=[]

x=int(input("enter number of elements to be added to the list:"))
for i in range(x):
    e=input("enter element:")
    testlist.insert(i,e)
print()     # adds an empty line 
print("Your list is",testlist)
