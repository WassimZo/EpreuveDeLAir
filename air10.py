import sys

def checkArgs() :
   if len(sys.argv) != 2 :
      return False
   return True

def createFile() :
   try :
      file = open(sys.argv[1], 'r')
   except FileNotFoundError :
      print("error")
      sys.exit()
   return file

def printContent(file) :
   print(file.read())

if checkArgs() :
   file = createFile()
   printContent(file)
   file.close()
else :
   print("error")
   sys.exit()