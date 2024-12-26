def longest_non_repeating_substring_sum(nums):
    """
    Calculates the sum of the longest non-repeating substring of a given list of numbers.
    """
    if not nums:
        return 0

    max_sum = 0
    current_sum = 0
    num_set = set()
    left = 0
    max_length = 0

    for right in range(len(nums)):
        while nums[right] in num_set:
            num_set.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        num_set.add(nums[right])
        current_sum += nums[right]
        max_length = max(max_length, right - left + 1)

        if len(list(num_set)) >= max_length:
            max_sum = max(max_sum, current_sum)

    return max_sum, max_length


nums = [1, 2, 3, 4, 5, 6, 4, 65, 9, 3, 56, 1, 90]
print(longest_non_repeating_substring_sum(nums))
