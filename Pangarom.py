
def is_pangram(input_string):

    v = set(input_string.lower())
    print(v)
    return "is a pangram" if set('abcdefghijklmnopqrstuvwxyz') <= set(input_string.lower()) else "not pangram"


input_string= "The quick brown fox jumps over the lazy dog"
my_string = 'assd'
print(is_pangram(input_string))
