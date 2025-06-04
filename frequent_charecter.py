text = "Random texT to checkkK"

freq = {}

for i in text:
    if i.isalpha():
        lower_i = i.lower()
        if lower_i not in freq:
            freq[lower_i] = 1
        else:
            freq[lower_i] += 1
print(freq)
top_value = 0
for v in freq.values():
    if v > top_value:
        top_value = v
print(f"top_value : {top_value}")
results = [k for k, v in freq.items() if v == top_value]
print("highest frequency letters : ", ", ".join(results))
