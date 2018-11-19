# Python dictionary and associated methods

dict={}
dict['one'] = 'This is one'
dict[2]     = 'This is two'

tinydict = {'Name':'John','id':6734,'dept':'sales'}

print(dict)
print(tinydict)
print(dict[2])

# this is how you can access keys and values 
print(list(tinydict.keys()))
print(list(tinydict.values()))

# adding to tinydict
tinydict['global'] = 'yes'
print(tinydict)

# updating dict
dict[2] = 'This is three'
print('the updated dictionary dict is:',dict)

