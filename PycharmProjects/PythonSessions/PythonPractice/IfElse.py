x=int(input("Enter value of x"))
if(x<0):
    print("x is negative number")
elif(x>0):
    print("x is positive number")
elif(x==0):
    print("x is equal to Zero")
else:
    print("x is Indefinite number")

#To find the highest number
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
if(a>b and a>c):
    print("a is highest number")
elif(b>c):
    print("b is highest number")
else:
    print("c is the highest number")