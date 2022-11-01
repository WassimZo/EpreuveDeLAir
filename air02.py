import sys

def checkNbArguments() :
   return len(sys.argv) > 2

def createStringTable(array) :
   return array[1:-1]

def getSeparator(array) : 
   return array[-1]

def createString(array, separator) :
   result=""
   for string in array :
      result = result + string + separator
   return result
 

if checkNbArguments() :
   table = createStringTable(sys.argv)
   separator = getSeparator(sys.argv)
   string = createString(table, separator)
   print(string)
else : 
   print("error")
   sys.exit()