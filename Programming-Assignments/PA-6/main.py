# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
# 2. Write a Python Program to Find Factorial of Number Using Recursion?
# 3. Write a Python Program to calculate your Body Mass Index?
# 4. Write a Python Program to calculate the natural logarithm of any number?
# 5. Write a Python Program for cube sum of first n natural numbers?

import math

# 1.
def fibonacciSeries(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)

n=10
for i in range(n):
    print(fibonacciSeries(i), end=' ')




# 2.
def factorial(n):
    if n==0 or n==1:
        return 1
    
    return factorial(n-1) * n

fact = factorial(4)
# print(fact)


# 3.
def bmi(height:float, weight:float):
    val = weight/(height/100)**2

    if val < 18.5:
        return f"{val} : underweight"
    elif val >= 18.5 and val <= 24.9:
        return f"{val} : Normal"
    elif val >= 25 and val < 29.9:
        return f"{val} : Overweight"
    elif val >= 30:
        return f"{val} : Obese"
        
h = 160 # cm
w = 61 # kg

status = bmi(h,w)
# print(status)

# 4.
def logOfNatural(number):
    return math.log(number)


# 5.
def cubeSumOfNaturalNo(number):
    cubeArr = [num**3 for num in range(1,number+1)]
    totalSum = 0
    for cube in cubeArr:
        totalSum += cube
    return totalSum
cubeSum = cubeSumOfNaturalNo(5)
# print(cubeSum)