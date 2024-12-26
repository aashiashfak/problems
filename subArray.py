nums = [1, -1, 5, -2, 3]
from copy import deepcopy

0

def find_largest_sub_array(nums):
    max_length = 0
    current_sum = 0
    targetSum = 3
    largest = []
    longest_sub = []
    for left in range(len(nums)):
        sub_arr = []
        sub_arr.append(nums[left])
        for right in range(len(nums)):
            if nums[left] + nums[right] <= targetSum:
                sub_arr.append(nums[right])   
            if sum(sub_arr) == targetSum:
                max_length = max(max_length, len(sub_arr))
                new_sub = deepcopy(sub_arr)
                largest.append(new_sub)
        sub_arr.clear()

    for i in largest:
        if len(i) == max_length:
            longest_sub = i
    return longest_sub

print(find_largest_sub_array(nums))
