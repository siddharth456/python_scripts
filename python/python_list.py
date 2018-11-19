#!/usr/bin/python3.6

#raw_input()

list = ['abcd',123,876,'jp','j_','_']
tinylist = ['hello',700]
testlist = ['C++','Java','Python']
testlist1 = [572,122,700]

print(list)
print(tinylist)
print(list[0])
print(list[5])
print(list[-2])
print(list[1:3])
print(list[2:])
print(tinylist *2)
print(list+tinylist)

# update list
list[3]='sid'
print(list)

# delete from list
del list[5]
print(list)

# length of list
print("length of list: ",len(list))
print("length of tinylist: ",len(tinylist))

# max value in list
print("max value in testlist: ",max(testlist))
print("max value in testlist1: ",max(testlist1))

# min value in list
print("min value in testlist: ",min(testlist))
print("min value in testlist1: ",min(testlist1))
