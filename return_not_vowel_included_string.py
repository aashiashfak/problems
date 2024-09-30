
list_1 = ["My", "Hai", "Dry", "sync", "Are", "You",]

stringVowel = "aeiou"

vowel_string = []

for word in list_1:
    flag = 0
    for c in word:
        if c.lower() in stringVowel: 
            flag = 1
    if flag == 0:    
        vowel_string.append(word)       

print(vowel_string)

def has_no_vowels(word):
    return all(char not in 'aeiouAEIOU' for char in word)

non_vowel_strings = list(filter(has_no_vowels, list_1))
print(non_vowel_strings)