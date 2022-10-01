#function isEven that takes a number as an argument
def isEven(num):
    
    #evaluates the expression and return its result
    #for even numbers num % 2 will be equal to 0, so it will return True, else False
    return num % 2 == 0

#function isOdd that takes a number as an argument    
def isOdd(num):
    
    #evaluates the expression and return its result
    #for odd numbers num % 2 will not be equal to 0, so it will return True, else False
    return num % 2 != 0
 
#function isPrime that takes a number as an argument    
def isPrime(num):
    
    # defining a flag variable
    flag = False
    
    #if num is equal to 1 return False
    if(num == 1):
        return False
        
    #if num is greater than 1, as all prime numbers are
    elif num > 1:
        #checking  for factors
        for i in range(2, num):
            if (num % i) == 0:
                
                # if factor is found, set flag to True
                flag = True
                
                # break out of loop
                break
    #returning the opposite of flag value
    #if factor is found flag will be True, but it will not be a prime Number
    #if factor is not found flag will be Fals, but it will be a prime Number
    return (not flag)

#opeining the file "06.06 Numbers.txt" in reading mode  
inputFile = open("06.06 Numbers.txt","r")

#opening files to store even numbers, odd numbers and prime numbers
evenNumbersFile = open("06.06 Evennumbers.txt","w+")
oddNumbersFile = open("06.06 Oddnumbers.txt","w+")
primeNumbersFiles = open("06.06 Primenumbers.txt","w+")

#intitializing variable to keep count of different numbers
numCount = 0;
oddCount = 0;
evenCount = 0;
primeCount = 0;

#for loop to iterate thorough lines of inputFile
for line in inputFile:

    #stripping the line from any whitespace or next line character and converting to integer
    line = int(line.strip())
    
    #increment numCount by 1
    numCount += 1
    
    #if line is an even number
    if isEven(line):
        
        #writing to evenNumbersFile 
        evenNumbersFile.write(str(line) + "\n")
        
        #increment evenCount by 1
        evenCount += 1
    
    #if line is an odd number    
    elif isOdd(line):
        
        #writing to oddNumbersFile 
        oddNumbersFile.write(str(line) + "\n")
        
        #increment oddCount by 1
        oddCount += 1
      
    #if line is a prime numbers    
    if isPrime(line):
        
        #writing line to primeNumbersFiles 
        primeNumbersFiles.write(str(line) + "\n")
        
        #increment primeCount by 1
        primeCount += 1

#closing all files  
inputFile.close()        
evenNumbersFile.close()
oddNumbersFile.close()
primeNumbersFiles.close()

#displaying count of different numbers
print(evenCount,"even numbers")
print(oddCount,"odd numbers")
print(primeCount,"prime numbers")
print(numCount,"number read")