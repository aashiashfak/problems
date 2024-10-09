arr = [10,2,3,4,5,6,9,8, 11]

def find_sec_largest(arr):
    max = sec_max = float('-inf')
    for i in arr:
        if i > max:
            sec_max , max = max , i 
        elif sec_max < i < max:
            sec_max = i

    return sec_max

print(find_sec_largest(arr))