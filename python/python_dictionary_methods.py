# dictionary methods 

# fromkeys() and copy() methods
# Sequence can be either list or tuple

seq=['Name','Age','Sex']
dict1,dict2={},{}
dict1=dict1.fromkeys(seq)
print("the dictionary created from sequence is dict1:",dict1)
dict2=dict1.copy()
dict2=dict2.fromkeys(seq,10)
print("the copy of dictionary dict1 with values for every key is dict2:",dict2)

# get() method gets value of key 

print("Value of dict2.get(\'Name\'):",dict2.get('Name'))
print("Value of dict1.get(\'Name\'):",dict1.get('Name'))

# Returns the default value in case key not found in dictionary
print("Value of dict2.get(\'School\'):",dict2.get('School',"NA"))

# has_key() depricated in python3,instead use in
print('Age' in dict1)

# items() method returns a list of dict (key,value) tuples
print("dict2.items():",dict2.items())

# update() method
dict3={'Name':'Anil','Age':23}
dict4={'Sex':'Male'}
dict3.update(dict4)
print("updated dict3:",dict3)
 

  
