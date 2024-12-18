list1 = [1,3,4,5,78,0, 5]


#secon largest
def find_sec_largetst(nums):
    nums.sort()
    return nums[len(nums)-2]
    
print("sec largest", find_sec_largetst(list1))

list1 = [1,3,4,5,78,0, 5, 8,5]


#first repeating value
def first_repeating_values(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return i 
        else:
            seen.add(i)
print("first repating value", first_repeating_values(list1))


# largest word
text = "hello world!, kdsfsdfsd "

# function to find the largest word
def largest_word(text):
    words = text.split(' ')
    largest_word = words[0]
    
    for word in words:
        if len(word) > len(largest_word): 
            largest_word = word  
    
    return largest_word
        
print("Largest word:", largest_word(text))
