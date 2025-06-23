arr = [2, 4, 5, 7, 8]
def remove_nth_element(n):
    for i in range(len(arr)):
        if i == n:
            arr.pop(i)
    return arr

print(remove_nth_element(3))


