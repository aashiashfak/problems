def find_target_sum_index(arr, target):
    two_sum = {}
    for i, num in enumerate(arr):
        value = target - num
        if value in two_sum:
            return [{value:two_sum[value]}, {num: i}]
        two_sum[num] = i

print(find_target_sum_index([2,  11, 15, 7], 9))
