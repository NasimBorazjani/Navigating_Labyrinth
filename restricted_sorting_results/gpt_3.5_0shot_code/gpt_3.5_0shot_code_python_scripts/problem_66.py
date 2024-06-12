
stacks = [[], [], ['White', 'Black', 'Green', 'White', 'Green', 'Blue'], ['Red', 'Green', 'Black', 'Red', 'White', 'Yellow'], [], ['Yellow', 'Black', 'Yellow', 'Red', 'Green', 'White'], [], ['White', 'Blue', 'Red', 'Red', 'Blue', 'Black'], [], ['Yellow', 'Blue', 'Yellow', 'Blue', 'Green', 'Black']]
costs = {0: 4, 1: 5, 2: 2, 3: 10, 4: 6, 5: 8, 6: 2, 7: 11, 8: 2, 9: 8}

transfer_pairs = []

def get_block_shade(block):
    if block:
        return block[0]
    return None

def calculate_cost(block, dest_stack):
    if not dest_stack:
        return 1
    dest_shade = get_block_shade(dest_stack)
    if not dest_shade or block == dest_shade:
        return 1
    return costs[stacks.index(dest_stack)]

while any(stacks):
    min_cost = float('inf')
    min_source = None
    min_dest = None

    for i, stack in enumerate(stacks):
        if stack:
            block = stack[0]
            for j, dest_stack in enumerate(stacks):
                if i != j:
                    cost = calculate_cost(block, dest_stack)
                    if cost < min_cost:
                        min_cost = cost
                        min_source = i
                        min_dest = j

    transfer_pairs.append((min_source, min_dest))
    stacks[min_dest].insert(0, stacks[min_source].pop(0))

print(transfer_pairs)
