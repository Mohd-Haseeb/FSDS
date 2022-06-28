# 1. Write a Python Program to Find LCM?
# 2. Write a Python Program to Find HCF?
# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# 4. Write a Python Program To Find ASCII value of a character?
# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?


# 1. and 2.
def gcd(a,b):
    
    if a==0 :
        return b
    if b==0:
        return a
    
    if a==b:
        return a

    if a>b:
        return gcd(a-b,b)
    
    return gcd(a,b-a)

gcdOf = gcd(36, 60)
# print(gcdOf)


# a*b = lcm(a,b) * hcf(a,b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

lcmOf = lcm(15,20)
# print(lcmOf)



# 3.

def  decimalToBinary(num):
    if num >= 1:
        decimalToBinary(num//2)
    print(num%2, end=' ')

# decimalToBinary(344)
# print(binary)

def decimalToOctal(num):
    countVal = 1
    octalVal = 0

    while num!=0:
        rem = num%8
        octalVal += (rem*countVal)
        countVal = countVal * 10
        num //= 8
    
    print(octalVal)



print()
# decimalToOctal(33)
# print(octal)

def decimalToHexa(num):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}

    hexaVal = ''
    while num > 0:
        rem = num % 16
        hexaVal = conversion_table[rem] + hexaVal
        num //= 16
    print(hexaVal)

decimalToHexa(10)

# 4.
def asciiValOf(character):
    return ord(character)

asciiVal = asciiValOf('A')
# print(asciiVal)


# 5.

def simpleCalculator():
    flag = True
    ans = 0

    while flag:
        number1 = int(input("Enter the number.\nOr do you want to quit?(0) -> "))
        if number1==0:
            flag= False
            break

        operand = input("Enter the operation to be performed (+, -, *, /, %) -> ")

        if operand not in ['+', '-', '*', '/', '%']:
            return "Something went wrong!!!"

        number2 = int(input("Enter the number.\nOr do you want to quit?(0) -> "))
        if number1==0:
            flag= False
            break
        
        if operand=="+":
            return number1+number2
        elif operand=="-":
            return number1 - number2
        elif operand=="*":
            return number1 * number2
        elif operand=="/":
            return number1 // number2
        elif operand=="%":
            return number1 % number2
        
        return "Something went wrong!!!"

value = simpleCalculator()
print(value)


