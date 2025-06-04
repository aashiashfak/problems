def glass_pattern_decorator(fn):
    def wrapper(*args, **kwargs):
        k = 0
        l = 9
        for i in range(l):
            if i <= l // 2:
                k += 1
            else:
                k -= 1
            for j in range(l):
                fn(i, j, k, l)
            print()

    return wrapper


# full hour glass
@glass_pattern_decorator
def full_hour_glass(i, j, k, l):
    if j < k - 1 or j > l - k:
        print(" ", end=" ")
    else:
        print("*", end=" ")


full_hour_glass()
print()


# hour glass  outerline
@glass_pattern_decorator
def hour_glass_with_outerline(i, j, k, l):
    if i == 0 or i == l - 1:
        print("*", end=" ")
    elif j == k - 1 or j == l - k:
        print("*", end=" ")
    else:
        print(" ", end=" ")


hour_glass_with_outerline()
print()


# butterfly pattern outerline
@glass_pattern_decorator
def butterfly_outline(i, j, k, l):
    if j == k - 1 or j == l - k or j == 0 or j == l - 1:
        print("*", end=" ")
    else:
        print(" ", end=" ")


butterfly_outline()
print()


@glass_pattern_decorator
def butterfly(i, j, k, l):
    if j <= k - 1 or j >= l - k:
        print("*", end=" ")
    else:
        print(" ", end=" ")

butterfly()
