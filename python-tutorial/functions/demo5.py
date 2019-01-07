# Global and local variables

a=10
b=20

# function defination
def show():
    print(a) #10
    global b
    b+=5;
    print(b)

# calling functions
show()