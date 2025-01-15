def missingNumber(nums):
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i
nums = [0, 1, 2, 4, 6, 3, 7]
print(missingNumber(nums)) 


