NOT DONE

__author__ = "Amber Williamson"
__licence__ = "GPL"
__version__ = "1.0.1"
__email__ = "amber.williamson@education.nsw.gov.au"
__status__ = "Production, Prototype or Development"

start = True
        
def sumArray(nootArray):
    sum = 0
    for number in nootArray:
        sum = sum + number
    print(sum)

def printArray(nootArray):
    kString = ""
    for number in nootArray:
        kString = kString + str(number) + " "
    print(kString)
    numberElements = len(nootArray)
    print('You have {} numbers in your array'.format(numberElements))
    
def loadArray(nootArray):
        boiArray.append(numbs)
        print(boiArray)
        numElements = len(nootArray)
        print('You have {} numbers in your array'.format(numElements))
        
def maxArray(nootArray):
    print("The max of your array is" , max(boiArray))
    
def minArray(nootArray):
    print("The min of your array is", min(boiArray))
    
#credit to Caitlin for the try and except part
boiArray = []
while start:
    user = input('Do you want to (l)oad numbers, (p)rint the array, (s)um the array, (f)ind the max of the array, f(i)nd the min of the array or (q)uit ')
    if user == 'l':
        try:
            numbs = int(input('Input a number that will be put into the array: '))
        except ValueError:
          print("Please enter an int")
        else:
            loadArray(boiArray)
    elif user == 'p':
        printArray(boiArray)
    elif user == 's':
        sumArray(boiArray)
    elif user == 'f':
        maxArray(boiArray)
    elif user == 'i':
        minArray(boiArray)
    elif user == 'q':
        start = False

