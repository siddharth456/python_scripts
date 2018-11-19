# demonstrating pass by reference just that the referenced object changes in the function

mylist=[10,20,30]
def changelist(mylist):
# referencing to a new object
   mylist=[1,2,3,4]
   print("the list is:",mylist)
changelist(mylist)
print("the list outside the function is:",mylist)
