# def find_sec_largest():
#     # Find the second largest number in a list
#     lst = [4, 2, 9, 6, 5, 1]
#     lst.sort()
#     return lst[-2]

# print(find_sec_largest())


# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]


# def find_common(q,s,d):
#     for i in q :
#         if i in s and i in d :
#             print(i,end=" ")
#     return
# find_common(ar1,ar2,ar3)


# def swap_sample_with_duplicates(sample):
#     swapped = {}
#     for key, value in sample.items():
#         if value in swapped:
#             swapped[value].append(key)
#         else:
#             swapped[value] = [key]
#     return swapped

# sample = {'1': 'a', '2': 'b', '3': 'a'}
# print(swap_sample_with_duplicates(sample))


# my_tuple = (10, 20, 30)
# print(my_tuple[0])  # Output: 10

# my_list = [ 10, 20]
# start, end = my_list
# print(start, end)

# word = "hello"
# print(word[::-1])

# word = "hello"
# reversed_word = ""

# for char in word:
#     reversed_word = char + reversed_word

# print(reversed_word)


# def longest_consecutive(arr):
#     nums = set(arr)
#     longest = 0

#     for num in nums:
#         if num - 1 not in nums:
#             length = 1
#             while num + length in nums:
#                 length += 1
#             longest = max(longest, length)

#     return longest


# arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 11]
# print(longest_consecutive(arr))


word = "HAPPYp"

freq = {}

for i in word.lower():
    freq[i] = freq.get(i, 0) + 1
    
print(freq)