children = 8
candies = 14

def can_distribute_equally(k, c):
    return k % c == 0

print(can_distribute_equally(candies, children)) 