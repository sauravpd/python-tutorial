# File Handling example
from io import open

text='File Handling example'

#open the file for writing
file=open('writeFileExample.txt','w')

#write content to the file
file.write(text)

#close file
file.close()