# exception handlnig example
try:
    print('try block')
    print('''
    this is
    multi
    line
    print
    example
    +++++++++++++++++++++++++
    | Multi line  print     |
    |                       |
    +++++++++++++++++++++++++
    ''')

except Exception as e:
    print(e)