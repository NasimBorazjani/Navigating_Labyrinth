
stacks = [[], [], ['Green', 'Red', 'Black', 'Blue', 'Blue'], ['Yellow', 'Blue', 'Blue', 'Green', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Red', 'Black'], [], [], ['Red', 'Green', 'Green', 'Red', 'Black']]
costs = {0: 2, 1: 3, 2: 9, 3: 8, 4: 3, 5: 7, 6: 9, 7: 5}

def get_top_block(stack):
    if stack:
        return stack[-1]
    return None

def get_cost(source, target):
    if not source:
        return 0
    if not target or get_top_block(target) == get_top_block(source):
        return 1
    return costs[target]

transfers = []

for i in range(8):
    for j in range(8):
        if i != j:
            while stacks[i] and (not stacks[j] or get_top_block(stacks[j]) == get_top_block(stacks[i])):
                transfers.append((i, j))
                stacks[j].append(stacks[i].pop())
                
total_cost = sum(get_cost(i, j) for i, j in transfers)
print(transfers)
print("Total cost:", total_cost)
