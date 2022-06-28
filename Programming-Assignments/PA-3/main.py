# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# 2. Write a Python Program to Check if a Number is Odd or Even?
# 3. Write a Python Program to Check Leap Year?
# 4. Write a Python Program to Check Prime Number?
# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# 1.
from calendar import isleap
from cmath import sqrt
import math
from operator import truediv

from numpy import mat


numberIs = lambda x : "Positive" if x>0 else "Zero" if x==0  else "Negative"

# print(numberIs(0))

# 2.
isOdd = lambda x : False if x%2==0 else True

number = 6623
if (isOdd(number)):
    print(f"{number} is odd")
else:
    print(f"{number} is Even")


# 3.

def isLeapYear(year:int):
    if year%4==0 and year%100 != 0:
        return "leap year"
    elif year%400 == 0 and year%100==0:
        return "leap year"
    else:
        return "Not a leap year"

leapyear = isLeapYear(2000)
# print(leapyear)



# 4
def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    boundary = math.floor(math.sqrt(n))
    for i in range(3, boundary+1,2):
        if n%i==0:
            return False
    return True

# print(isPrime(11))

# 5.
def generatePrimeNo(start, end):
    if start <2:
        start = 2
    primeArr = [i for i in range(start, end+1)]

    boundary = math.floor(math.sqrt(end))
    for i in range(2,boundary+1):
   
            
            for j in range(i**2,end+1,i):
                if j in primeArr:
                    primeArr.remove(j)

    for number in primeArr:
        print(number, end=' ')

generatePrimeNo(1,15)


# q = ("ineuron")
# print(type(q)) => why string?