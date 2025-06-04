# total operation to reach a number

# number = 15
# count = 0
# current = 1
# while current < number:
#     if current > 1 and current * current <= number:
#         current = current * current
#         print("in multiple ", current)
#     else :
#         current += 1
#         print("in addtion ", current)
#     count +=1
# print(count)


from collections import deque


def min_operations_to_reach(target):
    queue = deque([(1, 0)])  # (current_value, operation_count)
    visited = set()

    while queue:
        current, count = queue.popleft()
        if current == target:
            print("1st", current)
            return count
        if current > target or current in visited:
            print("2nd",current)
            continue
        visited.add(current)
        queue.append((current + 1, count + 1))
        if current > 1 and current * current <= target:
            print("3rd", current)
            queue.append((current * current, count + 1))


print(min_operations_to_reach(15))  # Output: minimal steps
