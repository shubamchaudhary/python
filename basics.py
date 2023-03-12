#PYTHON
a=5
str="abc"
print(a,str)
#print
print("A value is {} and string is {}".format(a,str))

#function in python
def addtwo(a,b):
    return a+b
print(addtwo(8,9))

def function(a,b):
    if(a%2):
        return a+b
    else:
        return a-b
print(function(3,7))

#while loop in python
i=0
sum=0
while i<100:
    sum+=i
    i+=1
print(sum)

#Lists in python
a=[1,2,8,5,3,9,0,11,12,13,14,15,21,23,22,24,31,24]
print(a)
#sort an array in ascending order
a.sort()
print(a,max(a),min(a))
#sorting in decending order
a.sort(reverse=True)
print(a,max(a),min(a))
#sorting using comparator
def sod(n):
    sum=0
    while n:
        sum+=n%10
        n/=10
    return sum
a.sort(key=sod)
print(a)

#slicing
#format..... [start(inclusive) : end(exclusive) : step]
print(a[1:2:1])
#with negative indexing
print(a[-1::-2])

#set
#properties: 
# 1.doesnt allow duplicate values, 
# 2.Stores values in sorted manner





#dictionary
dict={"a":1,"b":2,"c":3,7:"abcd"}
print(dict)

#class in python
class student:
    regnp=1
    name="abc"
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def __str__(self):
        return "Name is : {} and regno is : {}".format(self.name,self.regno)
s=student("Shubam",922055)
print(s.name,s.regno)
print(s)


#string to date-time obj
#date time obj to string