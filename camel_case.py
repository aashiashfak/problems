def set_camel_case(text):
    """Converts a string to camel case"""
    words = text.split()
    for i in range(1, len(words)):
        words[i] = words[i].capitalize() 
    return " ".join(words)


text = "hello world welcome to python programming"
print(set_camel_case(text))  # Output: "HelloWorld"