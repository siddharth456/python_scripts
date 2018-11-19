# Here we are demonstrating that all parameters in python are passed by reference

mylist=[10,20,30]
def changelist(mylist):
    print("the list before change:",mylist)
    mylist[2]=50
    print("the list after change:",mylist)
changelist(mylist)
print("the list outside the function:",mylist)
