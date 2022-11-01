import sys

def checkNbArguments() :
   return len(sys.argv) == 2

def correctString(string) : 
   index = 1 
   while index < len(string)-1 : 
      if string[index] == string[index-1] : 
         string = string[0:index] + string[index+1:]
      if string[index] == string[index+1] :
         string = string[0:index+1]+string[index+2:]
      index=index+1
   return string

if checkNbArguments() : 
   string = sys.argv[1]
   string = correctString(string)
   print(string)
else : 
   print("error")
   sys.exit()