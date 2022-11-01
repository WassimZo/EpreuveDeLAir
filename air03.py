import sys

def checkNbArguments() :
   return len(sys.argv) > 2

def checkPair(element, array, index) :
   for testElement in array[0:index] : 
      if testElement == element :
         return True
   for testElement in array[index+1:] : 
      if testElement == element :
         return True
   return False

def createTable(array) : 
   return array[1:]

def getElementWithNoPair(array) :
   result = []
   for element in array :
      index = array.index(element)
      if not checkPair(element, array, index) :
         result.append(element)

   return result

def printResult(array) : 
   result = ""
   for element in array :
      result = result + str(element) + " "
   print(result)


if checkNbArguments() :
   table = createTable(sys.argv)
   result = getElementWithNoPair(table)
   printResult(result)
else : 
   print("error")
   sys.exit()

