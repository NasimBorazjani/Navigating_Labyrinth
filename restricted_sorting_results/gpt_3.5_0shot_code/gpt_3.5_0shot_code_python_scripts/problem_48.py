
stacks = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], ['Green', 'Red', 'Black', 'Yellow', 'Blue'], ['Red', 'Green', 'Red', 'Black', 'Yellow']]
costs = {0: 2, 1: 4, 2: 5, 3: 2, 4: 2, 5: 3, 6: 2, 7: 5}

transfer_pairs = []

def get_top_block(stack):
    if stack:
        return stack[-1]
    return None

def get_cost(source, dest):
    if source == dest:
        return 0
    return costs[dest]

def find_cheapest_transfer():
    min_cost = float('inf')
    source_stack = None
    dest_stack = None

    for i in range(len(stacks)):
        for j in range(len(stacks)):
            if i != j:
                source_block = get_top_block(stacks[i])
                dest_block = get_top_block(stacks[j])

                if source_block and (not dest_block or source_block == dest_block):
                    cost = get_cost(i, j)
                    if cost < min_cost:
                        min_cost = cost
                        source_stack = i
                        dest_stack = j

    return source_stack, dest_stack

while any(stacks):
    source, dest = find_cheapest_transfer()
    transfer_pairs.append((source, dest))
    stacks[dest].append(stacks[source].pop())

print(transfer_pairs)
