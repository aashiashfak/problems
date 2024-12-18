name = "sa*h*al"
a = [i for i in name]

for i in range(len(a)):
    if a[i] == "*" :
        a[i-1] = "*"
    else:
        continue
al =  "".join(a)
al.replace("*", "")


