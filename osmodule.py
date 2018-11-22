import sys,os
cwd = os.getcwd()
print "current directory is : %s"%(cwd)

print(os.listdir('.'))
### os name
print (os.name)

### os.error() for printing the errors

### os.rename for rename of file in current directory
fd = "calc.py"
#os.rename(fd,'calculator.py') 

#print(os.environ())

path = os.getenv('PATH')
print path
print os.environ.get('PATH').split('/')

exists = os.path.isfile('fac.py')

if exists:
    print "exists"
else:
    print "not exists"


##############################

import os
from os.path import join, getsize
for root, dirs, files in os.walk('/root/Adithya_python_scripts'):
    print dirs,files
    #print root, "consumes"
    #print sum(getsize(join(root, name)) for name in files),
    #print "bytes in", len(files), "non-directory files"
