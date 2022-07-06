arr = [12,10,5,6,52,36]

for i in range(2):
    arr.append(arr[0])
    arr.remove(arr[0])

print(arr)