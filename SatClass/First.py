##Python basics
'''
 multi-line comment
'''
###Declaring variable
name="Richard"
num_1=12
num_2=3.14
status=False

print(type(num_1))
print(type(name))
print(type(status))
print(num_1+num_2)

##Functions
#returnig functions
def Subtraction():
    dif=num_1-num_2
    return dif
print(Subtraction())

#void functions
def Addition():
    sum=num_1+num_2
    print(sum)
Addition()