# Update string
var1='Hello World'
print ('Updated value:- ', var1[:6] + 'Python')

# String formatting
print('My name is %s and i am %i kg in weight'% ('Khan',71))

# Some built-in string methods

var2='this is a string example...wow!!!'
print ('Capitalize() example:',var2.capitalize())

sub='is'
print ('count(sub) example:',var2.count(sub))

print ('center() example:',var1.center(40,'$'))

sub1='!!'
print ('endswith(sub1) example:',var2.endswith(sub1))
print ('endswith(sub1,beg,end) example:',var2.endswith(sub1,0,10))

star='this\tis\tanother string example'
print ('expandtabs() example:',star.expandtabs())
print ('expandtabs(tabsize) example:',star.expandtabs(1))

# the find() method
print ('find() example:',var2.find(sub))
print ('find(sub,begin) example:',var2.find(sub,20))

# the index() method
print ('index() which is same as find() example:',var2.index(sub))

# comment the next line to avoid exception as per our scenario substring not found when begin index is 20
# print ('index(sub,begin) example:',var2.index(sub,20))

# is alphanumeric
test='thisstringisal8hanu5er1c'
print(test,test.isalnum())
test1='133...is a low score!!!!'
print(test1,test1.isalnum())

# is digit
test3='123456'
print(test3,test3.isdigit())
test4='this is not just 123 digit'
print(test4,test4.isdigit())

# only alphabets
test5='containsonlyalphabets'
print(test5,test5.isalpha())
test6=''
print(test6,test6.isalpha())
test7='\theloo'
print(test7,test7.isalpha())

# is numeric
testnum='123567'
print('testnum is numeric:',testnum.isnumeric())

# titlecased
test8='This String Is Titlecased'
print(test8,test8.istitle())
test9='this is not titlecased'
print(test9,test9.istitle())

# join(sequence)
str='-'
sequence=('hello','this','is','sequence')
print(str.join(sequence))

# left justified with padding
teststr='testing ljust() method with width 70 and fillchar *'
print(teststr.ljust(70,'*'))

# left strip 
teststr1='     \t\t   hello this is a test string'
print(teststr1.lstrip())

# is uppercase
upcase='THIS IS ALL UPPERCASE'
print(upcase,upcase.isupper())

# is lowercase
lower='this is all lowercase'
print(lower,lower.islower())

# contains only whitespaces
teststr3='      \t\t\n'
print(teststr3.isspace())

# max() min() string methods
teststr4='the zebra lives in safari...wow!!!'
print(teststr4,':',max(teststr4))
print('min(\'tutorial\'): '+min('tutorial'))

# right justified with padding
teststr='testing rjust() method with width 70 and fillchar *'
print(teststr.rjust(70,'*'))

# startswith() method
star1='this is a good day'
print(star1.startswith('this'))
print(star1.startswith('good',10,15))
print(star1.startswith('is',0,3))

# strip() method
star2="*********************hello world**************"
print(star2.strip('*'))

# swapcase() method
star3="this is a string example...wow!!!"
print(star3.swapcase())
star3=star3.title()
print(star3.swapcase())
