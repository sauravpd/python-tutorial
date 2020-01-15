# Exception handling
try:
    print('try block')
    a=10/0
except ZeroDivisionError as e:
    print('ZeroDivisionError found ',e)