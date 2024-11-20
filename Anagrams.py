def check_anagrams(word_1, word_2):
    """Check if two words are anagrams of each other."""
    def trim_word(word):
        return ''.join(sorted(word.lower().strip()))
    return trim_word(word_1) == trim_word(word_2)

word_1 = "listen       "
word_2 = "  silent"
print(check_anagrams(word_1, word_2))  # Output: True