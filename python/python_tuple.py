# tuples and associated methods

tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 , '13+4i'  ]
#tuple1[2] = 1000    # Invalid syntax with tuple
list1[2] = 1000     # Valid syntax with list
print(list1)
print(tuple1)
print(tuple1[2:])
print('tuple1 * 2:',tuple1 * 2)
print('length of tuple1 is:',len(tuple1))
print('Converting list1 to tuple:',tuple(list1))
del list1[3]
print('updated list after deletion:',list1)
