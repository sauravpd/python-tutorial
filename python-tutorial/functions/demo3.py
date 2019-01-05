# function parameter default example

# function definition
def add(num1,num2=10):
    print(num1)
    print(num2)
    result=num1+num2
    print("Addition is ",result)

# calling add function
add(20,40)# Addition is 60
add(10) # Addition is  20