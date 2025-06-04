l = 9
k = 0

# full hour glass


# def full_hour_glass(l, k):
#     for i in range(l):
#         if i <= l // 2:
#             k += 1
#         else:
#             k -= 1
#         for j in range(l):
#             if j < k - 1 or j > l - k:
#                 print(" ", end=" ")
#             else:
#                 print("*", end=" ")
#         print()


# full_hour_glass(l, k)
# print()
# hour glass with outerline


# def hour_glass_with_outerline(l, k):
#     for i in range(l):
#         if i <= 4:
#             k += 1
#         else:
#             k -= 1
#         for j in range(l):
#             if i == 0 or i == l - 1:
#                 print("*", end=" ")
#             elif j == k - 1 or j == l - k:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()


# hour_glass_with_outerline(l, k)
# print()


def butterfly_outline(l, k):
    for i in range(l):
        if i <= l // 2:
            k += 1
        else:
            k -= 1
        for j in range(l):
            if j == k-1 or j == l-k or j==0 or j==l-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

butterfly_outline( l, k )
print()  


def butterfly(l, k):
    for i in range(l):
        if i <= l // 2:
            k += 1
        else:
            k -= 1
        for j in range(l):
            if j == k - 1 or j == l - k or j == 0 or j == l - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


butterfly_outline(l, k)
