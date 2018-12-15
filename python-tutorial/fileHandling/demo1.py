# File Handling example
from io import open

text='File Handling example'
file=open('writeFileExample.txt','w')

file.write(text)

#close file
file.close()