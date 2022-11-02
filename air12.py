import sys

def checkArgs() :
   if len(sys.argv) < 2 :
      return False
   return True

def createArray(array) :
   args = []
   try :
      for nbr in array[1:] : 
         args.append(int(nbr))
   except ValueError :
      print("error")
      sys.exit()
   return args

def partition(array, low, high):
   pivot = array[high]
   indexLow = low-1
   for indexHigh in range(low , high) :
      if array[indexHigh] <= pivot :
         indexLow = indexLow+1
         (array[indexLow], array[indexHigh]) = (array[indexHigh], array[indexLow])
   (array[indexLow+1], array[high]) = (array[high], array[indexLow+1])
   return indexLow+1

def quickSort(array, low , high) :
   if low < high :
      pivotIndex = partition(array, low, high)
      quickSort(array, low, pivotIndex-1)
      quickSort(array, pivotIndex+1, high)

def printResult(array) :
   result=""
   for nbr in array : 
      result = result + str(nbr) + " "
   print(result)

if checkArgs() :
   args = createArray(sys.argv)
   quickSort(args, 0, len(args)-1)
   printResult(args)
else :
   print("error")
   sys.exit()
 
