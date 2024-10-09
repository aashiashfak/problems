# without set method

arr = [1,2,3,4,5,5,6,6,7,8,8,9,1]
l = len(arr)
i = 0 
while i < l :
    j = i+1
    while j < l:
        if arr[i] == arr[j]:
            arr.pop(j)
            l-=1
        else:
            j+=1 
    i+=1

print(arr)

# with set method
arr1 = [1,2,3,4,5,5,6,6,7,8,8,9,1]
set[arr1]
print(arr)


