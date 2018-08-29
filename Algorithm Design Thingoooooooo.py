NOT FINISHED

__author__ = "Amber Williamson"
__licence__ = "GPL"
__version__ = "1.0.1"
__email__ = "amber.williamson@education.nsw.gov.au"
__status__ = "Production, Prototype or Development"

dumbAssArray = []
def loadArray():
    print("loadArray was called")

def printArray():
    pass
    
a = input('Would you like to A - add numbers P - print our the array S - sum the array Q - quit ')
if a == '1':
   loadArray(theArray)
elif a == 'P':
   printArray()
elif a == 'S':
   sumArray()       
