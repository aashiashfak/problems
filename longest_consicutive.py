arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 11]

def longest_consecutive(arr):
    arr.sort()
    a =  list(set(arr))
    current_length = 1
    for i in range(1, len(a)):
        if a[i] - a[i - 1] == 1:
            current_length +=1
        else:
            break
    return current_length
print(longest_consecutive(arr))