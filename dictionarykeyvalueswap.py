sample = {'1':'a','2':'b' , '3':'c'}

def swap_sample (sample):
    for key,value in sample.items():
        sample[value] = sample.pop(key)
        sample[value] = key
    return sample
print(swap_sample(sample))