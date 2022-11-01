import sys 

def checkNbArgs() :
   return len(sys.argv) > 2

def createStringToVerify(array) :
   strings = []
   for string in array[1:-1] : 
      strings.append(string)
   return strings

def createVerifyingValue(array) :
   return array[-1]

def checkContaining(container, content) : 
   return container.find(content) != -1 or container.find(content.upper()) != -1

def CreateResultArray(array, verfyingValue) : 
   result = []
   for string in array : 
      if not checkContaining(string, verfyingValue) : 
         result.append(string)

   return result

def printResult(result) :
   string = ""
   for word in result : 
      string = string + word + "," + " "
   print(string[:-2])

if checkNbArgs() : 
   strings = createStringToVerify(sys.argv)
   verfyingValue = createVerifyingValue(sys.argv)
   result = CreateResultArray(strings, verfyingValue)
   printResult(result)
else : 
	print("error")
	sys.exit()
