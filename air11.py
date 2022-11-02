import sys

def checkArgs() :
   if len(sys.argv) != 3 :
      return False
   return True

def getNbStages(array) : 
   try :
      nbStages = int(array[2])
   except ValueError : 
      print("error")
      sys.exit()
   return nbStages

def getChar(array) :
   return array[1][0]

def createPyramid(char, nbStages) :
   stages = []
   leftSpace = 0
   rightSpace = 0
   charPerStage = (2*nbStages)-1
   while nbStages > 0:   
      stage = (leftSpace*' ')+(charPerStage*char)+(rightSpace*' ')
      stages.append(stage)
      charPerStage = charPerStage -2
      leftSpace = leftSpace +1
      rightSpace = rightSpace +1
      nbStages = nbStages -1
   return stages

def displayPyramid(pyramid) :
   for index in range(len(pyramid)-1, -1, -1) :
      print(pyramid[index])

if checkArgs() : 
   nbStages = getNbStages(sys.argv)
   char = getChar(sys.argv)
   pyramid = createPyramid(char, nbStages)
   displayPyramid(pyramid)
else :
   print("error")
   sys.exit()



