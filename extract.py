#!/usr/bin/env python
import os
import tika
import shutil
import time
from tika import parser
tika.TikaClientOnly = True
from datetime import datetime

headers = {
'X-Tika-PDFextractInlineImages': 'true',
}

#java -jar tika-server-1.22.jar --port 8001     #to start the server on port 8001
#'http://localhost:8001'        origin server code

fs = os.listdir('pdfs/') #list files in specified directory in a list

root = 'pdfs/'

fs = [f for f in fs if os.path.join(root, f) and (str(f).endswith('.pdf') or str(f).endswith('.docx') 
or str(f).endswith('.pptx') or str(f).endswith('.doc') or  str(f).endswith('.html') )] #using list comprehension to iterate through pdf and docx files

start = datetime.now()
for f in fs:
    d = os.path.join(root, f)
    frt = parser.from_file(d, serverEndpoint='http://localhost:8001/rmeta/text', headers=headers) #parse document file to tika server for text extraction
    data = str((frt["content"]))             #store extracted content from each file to variable data
    outfn = f[:-5] + '.txt'             #create a new file with filename and extension of .txt
    file = open(outfn, "w")             #open file in write mode
    file.write(data)                    #write content of data to opened file
    file.close()                        #close file
    shutil.move(outfn, 'text/')


end = datetime.now()            
print('done...')
print (end - start)