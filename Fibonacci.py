

def check_fibonacci (num):
    if num == 0: 
        return 0
    if num == 1:
        return 1
    a,b = 0, 1
    for i in range(2 ,num +1):
        a,b = b, a+ b
        print(a,b)

    return b
number = 7
print(check_fibonacci(number))