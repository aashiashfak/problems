def find_factorial( n ):
    if n == 0:
        return 1
    else:
        return n * find_factorial( n - 1 )
    
n = 5
print(find_factorial(n))  


def find_factorial_without_recurssion(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print( find_factorial_without_recurssion(5))