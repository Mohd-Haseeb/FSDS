# 1. Write a Python Program to Find the Factorial of a Number?
# 2. Write a Python Program to Display the multiplication Table?
# 3. Write a Python Program to Print the Fibonacci sequence?
# 4. Write a Python Program to Check Armstrong Number?
# 5. Write a Python Program to Find Armstrong Number in an Interval?
# 6. Write a Python Program to Find the Sum of Natural Numbers?

# 1.
def factorial(n):
    if n==0 or n==1:
        return 1
    
    return factorial(n-1) * n

fact = factorial(4)
# print(fact)


# 2.
def help(number,start):
    if start==11:
        return
    print(f"| {number} * {start} = {number*start} |")
    help(number,start+1)

def multiplicationTable(n):
    if n==0:
        return 0
    
    help(n,1)
    print("Completed")

# multiplicationTable(4)




# 3.
def fibonacci(n):
    if n==0 or n==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def printFibonaci(number):
    if number<=1:
        print("Enter valid number")
    
    for i in range(number):
        print(fibonacci(i), end=' ')

# printFibonaci(9)



# 4.
def isArmstrongNumber(number):
    add = 0
    temp = number
    count = 0
    while count<3:
        rem = number%10
        add += rem**3
        number //= 10
        count += 1
    if temp == add:
        return True
    else:
        return False 

ans = isArmstrongNumber(371)
print(ans)


# 5.
def generateArmstrongNumners(start,end):
    ans = []
    for i in range(start, end+1):
        if isArmstrongNumber(i):
            ans.append(i)

    return ans

res = generateArmstrongNumners(10,10000)
# print(res)


# 6.
def sumOfNaturalNo(number):
    if number == 1:
        return 1
    
    ans = sumOfNaturalNo(number-1) + number

    return ans

ans = sumOfNaturalNo(10)
print(ans)