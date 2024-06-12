
import heapq

def restricted_sorting(stacks, costs):
    # Step 1: Initialize a dictionary to keep track of the number of blocks of each color
    blocks_count = {}

    # Step 2: Iterate over the list of stacks and process each stack
    for i, stack in enumerate(stacks):
        for block in stack:
            # If the block is not in the dictionary, add it and initialize the cost to move it
            if block not in blocks_count:
                blocks_count[block] = [0, []]
            blocks_count[block][0] += 1
            if i not in blocks_count[block][1]:
                blocks_count[block][1].append(i)

    # Step 3: Iterate over the dictionary and transfer the blocks following the greedy approach
    transfer_pairs = []
    total_cost = 0
    for color, (count, stacks_with_color) in blocks_count.items():
        # Find the stack with the minimum cost that does not already have blocks of this color
        available_stacks = [(costs[j] if color not in stacks[j] else float('inf'), j) for j in stacks_with_color]
        heapq.heapify(available_stacks)
        while count > 0:
            try:
                cost, stack_index = heapq.heappop(available_stacks)
            except IndexError:
                break
            if cost == float('inf'):
                continue
            transfer_pairs.append((stacks_with_color[0], stack_index))
            total_cost += cost
            count -= 1

    return transfer_pairs, total_cost

stacks = [['Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'], [], [], ['Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'], ['Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'], [], ['White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'], [], [], ['Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'], ['Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'], []]
costs = [8, 5, 4, 12, 9, 9, 3, 2, 11, 9, 3, 2]
transfer_pairs, total_cost = restricted_sorting(stacks, costs)
print("Transfer pairs:", transfer_pairs)
print("Total cost:", total_cost)
