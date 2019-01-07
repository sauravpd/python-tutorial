# Global and local variables

a=10
b=20
def show():
    print(a) #10
    global b
    b+=5;
    print(b)
show()