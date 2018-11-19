# find all occurences of a search (sub)string in a given string

text='allow hello hallow'
index1=0

while index1<len(text):
     index1=text.find('ll',index1)
     if index1==-1:
        break
     print('ll found at index:',index1)
     index1+=2    # since len('ll')=2
