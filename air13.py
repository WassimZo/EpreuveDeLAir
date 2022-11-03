import os 
import subprocess

files = [
['air00.py', "\'Bonjour les gars\'", "Bonjour\nles\ngars"],
['air01.py', "\'Crevette magique dans la mer des étoiles\'", "la", "Crevette magique dans \n mer des étoiles"],
['air02.py', "Je", "teste", "des", "trucs" ,"\' \' ", "Je teste des trucs "],
['air03.py', "bonjour", "monsieur", "bonjour", "monsieur "],
['air04.py', "\'Hello milady,  bien ou quoi ??\'", "Helo milady, bien ou quoi ?"],
['air05.py', 1, 2, 3, 4, 5, "+2", "3 4 5 6 7 "],
['air06.py', "Michel", "Albert", "Therese", "Benoit", "t", "Michel"],
['air07.py', 1, 3, 4, 2, "1 2 3 4 "],
['air08.py', 10, 20, 30, "fusion", 15, 25, 35, "10 15 20 25 30 35 "],
['air09.py', "Michel", "Albert", "Therese", "Benoit", "Albert, Therese, Benoit, Michel"],
['air10.py', "a.txt", "je danse le mia"],
['air11.py', 0, 3, "  0  \n 000 \n00000"],
['air12.py', 6, 5, 4, 3, 2, 1, "1 2 3 4 5 6 "]
]

colors = ['\033[92m', '\033[91m', '\033[0m']
totalSucces = 0
totalTests = 0

def checkExistance(file) :
   global totalSucces
   global totalTests
   result = str(file[:-3]) + " 1/2 :"
   if os.path.exists(file) : 
      result = result+"%s success %s" %(colors[0], colors[2])
      totalSucces = totalSucces + 1
   else :
      result = result+"%s failure %s" %(colors[1], colors[2])
   totalTests = totalTests +1
   return result

def runTest(file) :
   global totalTests
   global totalSucces
   command = "python3 "+file[0]+' '
   result = str(file[0][:-3]) + " 2/2 :"
   for arg in file[1:-1] :
      command = command+' '+str(arg)
   exec = subprocess.getoutput(command)
   if str(exec) == str(file[-1]) :
      result = result+"%s success %s" %(colors[0], colors[2])
      totalSucces = totalSucces + 1
   else :
      result = result+"%s failure %s" %(colors[1], colors[2])
   totalTests = totalTests +1
   return result

def printResult(result) : 
   print(result)

result = ""
for file in files : 
   result = result + checkExistance(file[0])
   result = result + '\n'
   result = result + runTest(file)
   result = result + '\n'
result = result + '\n'+'Total succes: (%i/%i)' %(totalSucces, totalTests)
printResult(result)