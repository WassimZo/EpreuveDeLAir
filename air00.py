import sys

def split(string, separator) :
   result = []
   for char in string : 
      if char == separator :
         index = string.find(char)
         word = string[:index]
         result.append(word)
         string = string[index+1:]
   result.append(string)      

   return result

def checkNbArgs() :
   return len(sys.argv) == 2

def printResult() : 
   result = split(sys.argv[1], ' ')
   for word in result : 
      print(word)

if checkNbArgs() :
   printResult()
else : 
   print("error")
   sys.exit()