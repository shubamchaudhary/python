#TOPICS COVERED
# 1.Lambda Function
# 2.redex
# 3.Git
# 4.PIP
# 5.Django Begin

# 1.Lambda function-- used when function is to be used once in code
is_negative = lambda n : n<0
add_3 = lambda a,b,c : a+b+c
print(is_negative(-1))
print(add_3(1,2,3))

a=[1,2,-3,-4,0,-6,9,98,-76]
print(list(filter(is_negative,a)))

# https://www.w3schools.com/python/python_regex.asp go through this...

#lists
d={1:"a",2:"b","c":3}
print(d.values())
for key,value in d.items():
    print(key,value)

#traversing two lists at a time using zip
x = [1,2,3,4]
y=['a','b','c','d']
for i,j in zip(x,y):
    print(i,j)