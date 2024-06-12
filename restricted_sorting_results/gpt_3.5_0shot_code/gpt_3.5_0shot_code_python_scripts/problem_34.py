
stacks = [[], ['Yellow', 'Blue', 'Blue', 'Yellow', 'Green'], ['Black', 'Red', 'Black', 'Green', 'Red'], ['Yellow', 'Yellow', 'Red', 'Black', 'Blue'], [], ['Blue', 'Red', 'Green', 'Green', 'Black'], [], []]
costs = {0: 6, 1: 3, 2: 5, 3: 2, 4: 8, 5: 3, 6: 8, 7: 5}

def get_block_shade(block):
    if block:
        return block[-1]
    return None

def get_cheapest_transfer(source, target):
    min_cost = float('inf')
    cheapest_transfer = None
    for s in source:
        for t in target:
            cost = costs[t] if get_block_shade(s) == get_block_shade(t) or not t else costs[t] + 1
            if cost < min_cost:
                min_cost = cost
                cheapest_transfer = (source.index(s), target.index(t))
    return cheapest_transfer

transfers = []
while any(stacks):
    cheapest_transfer = get_cheapest_transfer([stack[-1] for stack in stacks if stack], [stack[-1] if stack else None for stack in stacks])
    transfers.append(cheapest_transfer)
    stacks[cheapest_transfer[1]].append(stacks[cheapest_transfer[0]].pop())

print(transfers)
