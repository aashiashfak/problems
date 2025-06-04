arr = [2, 5, 67, 7, 1, 4, 6]
def find_prime(arr):

    for i in range(len(arr)):
        is_prime = True
        if arr[i] <= 1:
            continue
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                is_prime = False
            break
        if is_prime:
            print(arr[i])


find_prime(arr)
