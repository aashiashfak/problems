words = ["iah woh era uoy", 'kkkk jjjjggg', "32413243453245"]

for sentence in words:
    for word in sentence.split():
        print(word[::-1], end=" ")

s = ["h", "e", "l", "l", "o"]
def reverseString(s):
    return s[::-1]

print(reverseString(s))