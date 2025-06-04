word = "samimas"

def check_palindrom(word):
    l = len(word)
    for i in range(l // 2):
        print(word[i], word[l - i - 1])
        if word[i] != word[l - i - 1]:
            return "this is not a palindrome"
    return "this is a palindrome"

print(check_palindrom(word))
