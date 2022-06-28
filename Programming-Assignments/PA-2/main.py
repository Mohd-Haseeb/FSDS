# 1. Write a Python program to convert kilometers to miles?
# 2. Write a Python program to convert Celsius to Fahrenheit?
# 3. Write a Python program to display calendar?
# 4. Write a Python program to solve quadratic equation?
# 5. Write a Python program to swap two variables without temp variable?


from cmath import sqrt
from datetime import date

# 1.
def km_to_miles(km):
    return km*(0.621371)

miles = km_to_miles(1)
# print(miles)


# 2.
def celsius_to_fahrenheit(degree):
    return (degree*1.8)+32

degree_f = celsius_to_fahrenheit(102)
# print(degree_f)



# 3.
def display_calendar():
    return date.today()

today = display_calendar()
print(today)


# 4.
def quadratic_quartion_root(a,b,c):
    """
        quadratic equation = a*X^2 + b*X + c
    """
    root_eq = (sqrt( (b**2) - (4*a*c)))
    root1 = (-b + root_eq) / (2*a)
    root2 = (-b - root_eq) / (2*a)

    return (root1,root2)

ans = quadratic_quartion_root(-2,2,1)
# print(ans)


# 5.
def swap_variables(x,y):
    x += y
    y = x-y
    x -= y
    print((f"x : {x} and y : {y}"))
    return (x,y)

swapped = swap_variables(29,54)
# print(swapped)
