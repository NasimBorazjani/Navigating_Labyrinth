
stacks = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
costs = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}

def get_block_shade(block):
    if block:
        return block[0]
    return None

def get_cheapest_transfer(source, target):
    min_cost = float('inf')
    cheapest_transfer = None
    for s in source:
        for t in target:
            if not t or get_block_shade(s) == get_block_shade(t):
                cost = costs[source.index(s)] + costs[target.index(t)]
                if cost < min_cost:
                    min_cost = cost
                    cheapest_transfer = (source.index(s), target.index(t))
    return cheapest_transfer

transfers = []
while any(stacks):
    cheapest_transfer = get_cheapest_transfer([stack[-1] if stack else None for stack in stacks], [stack[0] if stack else None for stack in stacks])
    transfers.append(cheapest_transfer)
    stacks[cheapest_transfer[1]].insert(0, stacks[cheapest_transfer[0]].pop())

print(transfers)