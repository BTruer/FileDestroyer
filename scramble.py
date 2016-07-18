import sys
import random
import string

def generateRandomText(size=9999, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def doIterations(filename, num=10):
    for j in range(0,num):
        textFile = open(fileName,'w')
        for i in range(0,100):
            text = generateRandomText()
            textFile.write(text+"\n")
        print("iteration " + j + " complete")
        textFile.close()

if len(sys.argv)==1:
    print("How to use:\n   python scrable.py 'filename' 'number of itterations to run (int)'")

if len(sys.argv)==2:
    fileName = str(sys.argv[1])
    doIterations(fileName)

elif len(sys.argv)==3:
    fileName = str(sys.argv[1])
    num = int(sys.argv[2])
    doIterations(fileName,num)
