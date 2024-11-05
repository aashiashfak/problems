def removeDuplicates(nums) -> int:
        if len(nums) == 0:
            return 0

        i = 0  
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        print('final array', nums)         
        return i + 1
    
nums =  [1,1,2]

print('final length', removeDuplicates(nums))
