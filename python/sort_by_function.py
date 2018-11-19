# this script demonstrates the sort() method in list

# first the default behaviour

alist=['actor','vinay','kumar','akila','suresh','babu','Si']
alist.sort()
print("the sorted list is:",alist)

# sort in descending order

alist.sort(reverse=True)
print("the list sorted in descending order:",alist)

# We create a function which will sort according to the object length
def myfunc(e):
    return len(e)
alist.sort(key=myfunc)
print("the list sorted as per object length:",alist)

# We create a function which will sort by taking the second element of a multi-dimensional list
def takeSecond(elem):
    return elem[1]
randomlist=[(1,3),(2,4),(1,1),(2,1)]
randomlist.sort(key=takeSecond)
print("sorted list:",randomlist)

