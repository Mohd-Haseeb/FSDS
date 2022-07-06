
# 1. Write a Python Program to find sum of array?
def sumOfArray(arr:list)->int:
    total = 0
    for element in arr:
        total += element
    return total

a = [1,4,7,8]
res = sumOfArray(a)
# print(res)



# 2. Write a Python Program to find largest element in an array?
def largestInArr(arr:list)->int:
    maximum = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum

a = [1,49,7,8]
# print(largestInArr(a))




# 3. Write a Python Program for array rotation?
def arrayRotation(arr:list,degree:int)->list:
    n = len(arr)
    rotated_arr = [0 for j in range(n)]
    for i in range(n):
        if i+degree <n:
            rotated_arr[i+degree] = arr[i]
        else:
            rotated_arr[i+degree-n] = arr[i]
    return rotated_arr

myArr = [5,8,12,16,19]
ans = arrayRotation(myArr, 5)
# print(ans)





# 4. Write a Python Program to Split the array and add the first part to the end?
def splitArr(arr:list,position:int)->list:
    
    for i in range(position):
        arr.append(arr[i])
    # print("Array before pop -> ", arr)
    arr = arr[position-1:]
        

    return arr

arr = [12,10,5,6,52,36]
position =3
ans = splitArr(arr,position)
print(ans)




# 5. Write a Python Program to check if given array is Monotonic?
def isMonotonic(arr:list)->bool:
    ans = True
    n = len(arr)
    if arr[0]<arr[1]:
        for i in range(1,n):
            if not(arr[i]>arr[i-1]) and ans:
                ans = False

    else:
        
        for i in range(1,n) and ans:
            if not(arr[i]<arr[i-1]):
                ans = False
    return ans

arr = [7,8,10,13,17]
res = isMonotonic(arr)
# print(res)