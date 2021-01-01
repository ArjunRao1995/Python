score=[10, 20,30,40,50]
#slicing 0 - 4
#slicing -1 -2 -3 -4 -5
print(score)
print(score[0])
print(score[-5])

print(score[:]) #new/shallow copy of list

#Concatenate
print(score + [1,2,3])
print(score + ["A","B", "C"])

#Strings are immutable we cannot change the vale once declared whereas Lists are mutable, we can change the content

number=[1,2,3,4,5]
number[2]=90
print(number)

#append
number.append(100)
number.append(7**3)
print(number)

#to replace name in range
name = ['a','b','c','d','e','f']
print(name)
name[2:5]=['C','D','E']
print(name)

#to remove name in range
name[2:5]=[]
print(name)

#to remove all
name[:]=[]
print(name)
name.append([1,2,3])
print(name)

test=[10,20,30,40,50,60]
print(len(test))

#nested lists
a=['a','b',3]
n=['x','y','0']
x=[a,n]
print(a)
print(x)
print(x[0][1])
print(x[1][0])