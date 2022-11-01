import sys 

def checkNbArgs() :
   return len(sys.argv) > 2


def createNumbersArray(array) :
   numbers = []
   try : 
      for value in array :
         number = int(value)
         numbers.append(number)
   except ValueError :
      print("error")
      sys.exit()
   return numbers

def createValue(strValue) :
   try : 
      intValue = int(strValue)
   except ValueError :
      print("error")
      sys.exit()
   return intValue


def calculate(array, operator, value) :
   result = [] 
   if operator == '+' : 
      for number in array :
         result.append(number+value)
      return result
   elif operator == '-' : 
      for number in array :
         result.append(number-value)
      return result
   else : 
      print("error")
      sys.exit()

def printResult(array) :
   result=""
   for nbr in array : 
      result = result + str(nbr) + " "

   print(result)


if checkNbArgs() :
   numbers = createNumbersArray(sys.argv[1:-1])
   operator = sys.argv[-1][0]
   value = createValue(sys.argv[-1][1:])
   numbers = calculate(numbers, operator, value)
   printResult(numbers)
else : 
   print("error")
   sys.exit()


