def glass_pattern_decorator(fn):
    def wrapper(*args, **kwargs):
        l = 9
        k = kwargs.get("k", 0)
        should_increment = kwargs.get("increment", True)
        for i in range(l):
            if i <= l // 2:
                if should_increment:
                    k += 1
                else:
                    k -= 1
            else:
                if should_increment:
                    k -= 1
                else:
                    k += 1
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


# hour glass  outerline
@glass_pattern_decorator
def hour_glass_with_outerline(i, j, k, l):
    if i == 0 or i == l - 1:
        print("*", end=" ")
    elif j == k - 1 or j == l - k:
        print("*", end=" ")
    else:
        print(" ", end=" ")


# butterfly pattern outerline
@glass_pattern_decorator
def butterfly_outline(i, j, k, l):
    if j == k - 1 or j == l - k or j == 0 or j == l - 1:
        print("*", end=" ")
    else:
        print(" ", end=" ")

# butterfly pattern
@glass_pattern_decorator
def butterfly(i, j, k, l):
    if j <= k - 1 or j >= l - k:
        print("*", end=" ")
    else:
        print(" ", end=" ")

# pattern X
@glass_pattern_decorator
def pattern_X(i, j, k, l):
    if j == k - 1 or j == l - k:
        print("*", end=" ")
    else:
        print(" ", end=" ")

# diamond pattern outerline
@glass_pattern_decorator
def diamond_outline(i, j, k, l):
    if j == k or j == (l - k) - 1:
        print("*", end="")
    else:
        print(" ", end="")

if __name__ == "__main__":
    pattern_X(increment=True)
    print()
    butterfly(increment=True)
    print()
    butterfly_outline(increment=True)
    print()
    full_hour_glass(increment=True)
    print()
    hour_glass_with_outerline(increment=True)
    print()
    diamond_outline(k=5, increment=False)
