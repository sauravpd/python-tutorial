# Exception handling
try:
    print('try block')
    a=10/0
except Exception as e:
    print('exception found ',e)