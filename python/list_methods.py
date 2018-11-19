# there are several list methods 

# the append() method
list1=['C++','Java','Python']
list1.append('C#')
print ('the updated/appended list:',list1)
print()

# the count() method
samplelist=[123,'abc','zara','ali',123]
print("the count of abc is: ",samplelist.count('abc'))
print("the count of 123 is: ",samplelist.count(123))
print()

# the extend() method
samplelist1=list(range(5))
samplelist.extend(samplelist1)
print('extended list: ',samplelist)
print()

# the index() method
testindex=[123,'hello',123,500,'world','Ali']
a=testindex.index(123)
b=testindex.index('world')
print('The pos of \'123\' in the testindex list is:',a)
print('The pos of \'world\' in the list is:',b)
print()

# the insert() method
testindex.insert(1,'The Da Vinci Code')
print('the new testindex list is:',testindex)
print()

# the pop() method
testindex.pop()
testindex.pop()
testindex.pop(0)
print('the testindex list after some popping:',testindex)
print()

# the reverse() method
alist=['Apple','Banana','Cotton','Zebra']
print("the original list is:",alist)
alist.reverse()
print("the reversed list is:",alist)
print()

# the remove() method
alist.remove('Cotton')
print('alist after removing the \'Cotton\' object:',alist)
print()

# the clear() method
alist.clear()
print("we emptied the alist:",alist)
 
# the sort() method
# demonstrated in another script named sort_by_function.py 
