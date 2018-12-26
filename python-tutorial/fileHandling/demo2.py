# File Handling example
from io import open

text='\npython file handling example'

#open the file for append
fileAppend=open('writeFileExample.txt','a')
fileAppend.write(text)
fileAppend.close()