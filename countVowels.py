text = "You are Awesome"
vowel = "aeiou"
count = 0
for i in text :
    if i.lower() in vowel:
        count += 1
        print(f"{count} : {i}")
        
print("total vowels in text are:", count)

