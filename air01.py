import sys

def splitWithArg(string, separator) :
   result = []
   while string.find(separator) != -1 :
      separatorLenght = len(separator) 
      result.append(string[0:string.find(separator)])
      string = string[separatorLenght+string.find(separator):]
   result.append(string)
   return result

def checkNbArgs() :
   return len(sys.argv) == 3

def printResult() : 
   result = splitWithArg(sys.argv[1], sys.argv[2])
   for word in result : 
      print(word)

if checkNbArgs() :
   printResult()
else : 
   print("error")
   sys.exit()