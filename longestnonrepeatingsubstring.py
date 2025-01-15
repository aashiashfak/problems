def lengthOfLongestSubstring(s):
    max_length = 0
    l = len(s)
    left = 0
    char_set = set()
    for right in range(l):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])

        max_length = max(max_length, right - left + 1)
    
    return max_length

print(lengthOfLongestSubstring("abaabacc"))




