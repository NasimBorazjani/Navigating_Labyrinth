
from collections import Counter

def restricted_sorting(stacks, costs):
    # Create a dictionary to store the blocks and their counts in each stack
    blocks_counts = [Counter(stack) for stack in stacks]

    # Initialize the result list
    result = []

    # Iterate over the dictionary
    for i in range(len(blocks_counts)):
        # Check if the stack is not empty and contains more than 3 blocks
        if blocks_counts[i]:
            # Find the most common block in this stack
            most_common_block = blocks_counts[i].most_common(1)[0][0]

            # Find the least cost stack to move the block to
            min_cost = float('inf')
            min_index = -1
            for j in range(len(blocks_counts)):
                if j != i and (not blocks_counts[j] or blocks_counts[j].most_common(1)[0][0] == most_common_block):
                    cost = costs[j]
                    if cost < min_cost:
                        min_cost = cost
                        min_index = j

            # Move the block from stack i to stack min_index
            if min_index != -1:
                blocks_counts[i][most_common_block] -= 1
                if not blocks_counts[i][most_common_block]:
                    blocks_counts[i].pop(most_common_block)
                if min_index not in blocks_counts or blocks_counts[min_index].most_common(1)[0][0] != most_common_block:
                    blocks_counts[min_index][most_common_block] = 1
                else:
                    blocks_counts[min_index][most_common_block] += 1
                result.append((i, min_index))

    return result

# Test the function
stacks = [['Red', 'Green', 'Green', 'Yellow'], [], ['Blue', 'Blue', 'Green', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Yellow'], []]
costs = [4, 1, 7, 3, 2, 2]
print(restricted_sorting(stacks, costs))
