arr = [10,2,3,4,5,6,9,8,11]


def remove_element(arr):
    i=0
    for i in range(len(arr)): 
        if i>=len(arr)-1:
            break
        if arr[i] % 3 == 0 and i < 1:
            arr.pop(i + 1)
    return arr


print(remove_element(arr))

