word = 'HAPPYp'


result = {}
for i in word.lower():
    if i in result:
        result[i] += 1
    else :
        result[i] = 1
print(result)




