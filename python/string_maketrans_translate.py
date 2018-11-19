# charcter mapping(intab/outtab) to create translate table using maketrans() method

intab="aeiou"
outtab="12345"

transtab=str.maketrans(intab,outtab)
print("This is transtab::",transtab)
# pass it to translate() method

str="This is a sample string....wow!!!"
print(str.translate(transtab))

