import sys

def checkNbArgs() :
   return len(sys.argv) > 2

def createList(array) :
   intArray = []
   try :
      for nbr in array[1:-1] :
         intArray.append(int(nbr))
   except ValueError :
      print ("error")
      sys.exit()
   return intArray

def getElementToInsert(array) :
   try :
      element = int(array[-1])
   except ValueError :
      print ("error")
      sys.exit()
   return element

def insertElement(element, array) :   
   array.append(element)
   index = len(array) - 1
   while array[index-1] > array[index] : 
      k = array[index]
      array[index] = array[index-1]
      array[index-1] = k
      index = index-1
   return array


def printResult(result) :
   string = "" 
   for nbr in result :
      string = string + str(nbr) + " "
   print(string)

if checkNbArgs() :
   intList = createList(sys.argv)
   element = getElementToInsert(sys.argv)
   intList = insertElement(element, intList)
   printResult(intList)

else :
   print("error")
   sys.exit()
