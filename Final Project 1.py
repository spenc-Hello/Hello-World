####################
#Hello World
#Did this work?
#Spencer 
####################

def initList(inFile):
    l=[]
    for line in inFile: 

        newLine=line.rstrip('\n') 
        row=newLine.split(',') 
        for temperature in row:
            l.append(int(temperature))
    return l

def getSize(aList):
  
    return len(aList)

def getHighest(aList):

    aList.sort()
  
    return aList[len(aList)-1]

def getLowest(aList):
    return min(aList)

def getAvearge(aList):
    average=sum(aList)/len(aList)
    return average

def main():
    fileName=input("enter file name: ")
    inFile=open(fileName,"r")
    aList=initList(inFile)

    print("size: ",getSize(aList))
    print("highest: ",getHighest(aList))
    print("lowest: ",getLowest(aList))
    print("average: ",getAvearge(aList))

main()