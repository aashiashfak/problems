word = "Hello "

upper = 0
lower = 0
for i in word:
    if i  != " ":
        if i.isupper():
            upper+=1
        else:
            lower+=1

print(f"count upper :{upper} ")
print(f"count lower :{lower} ")