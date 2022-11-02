import sys 

def checkArgs() :
   global indexOfSeparation
   indexOfSeparation = 0
   if len(sys.argv) > 3 :
      if "fusion" in sys.argv :
         indexOfSeparation = sys.argv.index('fusion')
         return True
   return False

def createFirstList(args) :
   firstList = []
   try :
      for nbr in args[1:indexOfSeparation] : 
         firstList.append(int(nbr))
   except ValueError :
      print("error")
      sys.exit()
   return firstList   

def createSecondList(args) :
   secondList = []
   try :
      for nbr in args[indexOfSeparation+1:] : 
         secondList.append(int(nbr))
   except ValueError :
      print("error")
      sys.exit()
   return secondList   

def sortedFusion(firstList, secondList) :
   sortedList = []
   firstIndex = 0
   secondIndex = 0
   while firstIndex < len(firstList) or secondIndex < len(secondList) :
      if firstIndex == len(firstList) : 
         for nbr in secondList[secondIndex:] :
            sortedList.append(nbr)
            secondIndex = secondIndex+1
      elif secondIndex == len(secondList) :
         for nbr in firstList[firstIndex:] : 
            sortedList.append(nbr)
            firstIndex = firstIndex+1
      else : 
         if firstList[firstIndex] < secondList[secondIndex] :
            sortedList.append(firstList[firstIndex])
            firstIndex = firstIndex+1
         elif firstList[firstIndex] == secondList[secondIndex] :
            sortedList.append(firstList[firstIndex])
            firstIndex = firstIndex +1 
            secondIndex = secondIndex +1
         else : 
            sortedList.append(secondList[secondIndex])
            secondIndex = secondIndex+1
   return sortedList   	


def printResult(result) :
   string = "" 
   for nbr in result :
      string = string + str(nbr) + " "
   print(string)


if checkArgs() :
   firstList = createFirstList(sys.argv)
   secondList = createSecondList(sys.argv)
   sortedList = sortedFusion(firstList, secondList)
   printResult(sortedList)
else : 
   print("error")
   sys.exit()


