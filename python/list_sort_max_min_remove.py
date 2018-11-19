testlist=[23,76,1,98,11,35]
trimmed=testlist[:]     # copy list to trimmed

# remove max/min item in the list
testlist.remove(max(testlist))
testlist.remove(min(testlist))

print("Original list:",trimmed)
print("list after max/min deletion:",testlist)     

'''Sorting the list'''
testlist.sort() 
print("sorted list:",testlist)
testlist.sort(reverse=True)
print("sorted list in reverse:",testlist) 
