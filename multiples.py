list_1 = [
    3,
    9,
    27,
    131,
    26,
    12,
    80,
    124,
    163,
    39,
]


def delete_multiple_of(n):
    return [i for i in list_1 if i % n != 0]


print(delete_multiple_of(3))
