def find_largest_sub_array(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    start, end, temp_start = 0, 0, 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i  
        else:
            current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i

    return max_sum, nums[start : end + 1]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, sub_array = find_largest_sub_array(nums)
print(f"Maximum Sum: {max_sum}, Subarray: {sub_array}")
