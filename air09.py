import sys 

def checkArgs() :
   if len(sys.argv) < 2 :
      return False
   return True

def createList(array) :
   return sys.argv[1:]

def rotation(array) :
   first = array.pop(0)
   array.append(first)
   return array

def printResult(result) :
   string = "" 
   for word in result :
      string = string + str(word) + ", "
   print(string[:-2])

if checkArgs() : 
   args = createList(sys.argv)
   result = rotation(args)
   printResult(result)
else :
   print("error")
   sys.exit()

   
   