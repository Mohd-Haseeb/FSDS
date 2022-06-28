
def sumOfNaturalNo(number):
    if number == 1:
        return 1
    
    ans = sumOfNaturalNo(number-1) + number

    return ans

ans = sumOfNaturalNo(3)
print(ans)