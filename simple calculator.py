def add(x,y):
    print("add 2 numbers")
    return x+y

def subtract(x,y):
    print("subtract 2 numbers")
    return x-y

def multiply(x,y):
    print("multiply 2 numbers")
    return x*y
    
def divide(x,y):
    print("divide 2 numbers")
    return x/y
x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
i=int(input("your choice=1/2/3/4: "))

if(i==1):
    k=add(x,y)
    print("sum is ",k)
    
if(i==2):
    k=subtract(x,y)
    print("subtract is ",k)
    
if(i==3):
    k=multiply(x,y)
    print("multiply is ",k)
    
if(i==4):
    k=divide(x,y)
    print("divide is ",k)
