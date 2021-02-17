#Hi, thanks for checking out my code! 
#This is a password generator I made that'll print a randomly generated password to the terminal
#Goal: make a 13>= digit password using uppercase, lowercase letters, and numbers


import random


#function to suffle password characters
#create a variable to create list from pwd argument
#random.shuffle with shuffle order of elements in list
#return an empty string, join list as string of characters
#this function will be used at the end of the program
def sufflePWD(pwd):
    pwdList = list(pwd)
    random.shuffle(pwdList)
    return ''.join(pwdList)


#create variable, random number, to determine how many uppercase,lowercase, number, and symbol characters to create
#j,k,m,t are 0, will be the counters
u = random.randint(4,8)
j = 0

l = random.randint(4,8)
k = 0

n = random.randint(4,8)
m = 0

s = random.randint(1,4)
t = 0


#create empty array for uppercase letters
numberOfUPL = []
#create empty list for lowercase letters
numberOfLCL = []
#create empty list for numbers
numberOfNums = []

#create list of acceptable symbols' ASCII code (since these characters ASCII numbers are consectuive like the letter and number characters)
#symbols are: !,.-?
symbolList = [33,44,45,46,63]
#create empty list for symbols
symbolListAdded = []


#add random ASCII uppercase characters as elements to list, increment counter by
while j < u:
    UPL = chr(random.randint(65,90))
    numberOfUPL.append(UPL)
    j+=1
#add random ASCII lowercase characters as elements to list, increment counter by
while k < l:
    LCL = chr(random.randint(97,122))
    numberOfLCL.append(LCL)
    k+=1
#add random ASCII number characters as elements to list, increment counter by
while m < n:
    Num = chr(random.randint(48,57))
    numberOfLCL.append(Num)
    m+=1
#add random ASCII symbol characters to list
#first, randomly choose index for elements in symbol list
#add that element/symbol to other list, after converting ASCII code to character
#increment counter
while t < s:
    SL = random.randint(0,4)
    symbolListAdded.append(chr(symbolList[SL]))
    t+=1


#remove brackets, single quotes, commas from list to string
newUPL = ''.join(numberOfUPL)
newLCL = ''.join(numberOfLCL)
newNums = ''.join(numberOfNums)
newSymbols = ''.join(symbolListAdded)


#concatenate string variables to create password
pw = newUPL + newLCL + newNums + newSymbols
#call shuffle function
pw = sufflePWD(pw)


#finally, print the password
print(pw)