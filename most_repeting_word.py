word = "cat dog cat fish dog dog cat"


def most_frequent_word(s):
    freq_words = {}
    words = s.split()
    for i in words :
        freq_words[i] = freq_words.get(i , 0) +1
    max_value = max(freq_words.values())
    most_freq = [word for word in freq_words if freq_words[word]== max_value]
    print(freq_words, max_value, most_freq)
most_frequent_word(word)
