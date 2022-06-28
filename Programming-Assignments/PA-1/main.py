
import random


# 1. Write a Python program to print "Hello Python"?
print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?
def operations(a:int,b:int) -> int:
    ans = (a+b)/2
    return ans

print(operations(5,6))

# 3. Write a Python program to find the area of a triangle?
def area_of_triangle(base,height) -> float:
    area = (base*height)/2
    return area

# 4. Write a Python program to swap two variables?
def swap(a,b):
    #method-1
    a += b
    b = a-b
    a -= b

    # method-2
    # a,b = b,a

    return (a,b)

# 5. Write a Python program to generate a random number?
swapped = swap(2018,9)
print("Swapped -> ",swapped)

def generate_random_number():
    number = random.randint(1,10000)
    return number

random_number = generate_random_number()
print("Random Number : ",random_number)


