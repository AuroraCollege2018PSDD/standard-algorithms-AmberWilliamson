__author__ = "Amber Williamson"
__licence__ = "GPL"
__version__ = "1.0.1"
__email__ = "amber.williamson@education.nsw.gov.au"
__status__ = "Production, Prototype or Development"

#subroutine
start = True
        
def sumArray(nootArray):
    sum = 0
    for number in nootArray:
        sum = sum + number
    print('The sum of your array is', + sum)

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
        print('You have {} number/s in your array'.format(numElements))
        
def findMax(nootArray):
    print("The max of your array is" , max(boiArray))
    print("findMax was called")
    
def findMin(nootArray):
    print("The min of your array is", min(boiArray))
    print("findMin was called")

def mainMenu(nootArray):
    user = input("This is the main menu, do you want to (l)oad numbers, (p)rint the array, (s)um the array, (f)ind the max of the array, f(i)nd the min of the array or (q)uit ")
    if user == 'l':
        try:
            numbs = int(input('Input a number that will be put into the array or press m to return to the main menu: '))
        except ValueError:
          print("Invalid entry, please enter a number or press m to return to the main menu")
        else:
            loadArray(boiArray)
    elif user == 'p':
        printArray(boiArray)
    elif user == 's':
        sumArray(boiArray)
    elif user == 'f':
        findMax(boiArray)
    elif user == 'i':
        findMin(boiArray)
    elif user == "m":
        mainMenu()
    elif user == 'q':
        start = False

    
    
#credit to Caitlin for the try and except part
#mainprogram
boiArray = []
while start:
    user = input("This is the main menu, do you want to (l)oad numbers, (p)rint the array, (s)um the array, (f)ind the max of the array, f(i)nd the min of the array or (q)uit ")
    if user == 'l':
        try:
            numbs = int(input('Input a number that will be put into the array '))
        except ValueError:
          print("Invalid entry, please enter a number")
        else:
            loadArray(boiArray)
    elif user == 'p':
        printArray(boiArray)
    elif user == 's':
        sumArray(boiArray)
    elif user == 'f':
        findMax(boiArray)
    elif user == 'i':
        findMin(boiArray)
    elif user == "m":
        mainMenu()
    elif user == 'q':
        start = False
