
import heapq

def restricted_sorting(stacks, costs):
    # Initialize an empty list to store the transfer pairs
    transfer_pairs = []
    
    # Iterate over the stacks
    for i in range(len(stacks)):
        # If the stack is not empty
        if stacks[i]:
            # Check if the top block is the same as the second block
            if stacks[i][-1] != stacks[i][-2]:
                # Find the stack with the same color block at the top
                for j in range(len(stacks)):
                    if j != i and stacks[j] and stacks[j][-1] == stacks[i][-1]:
                        # Move the top block to the stack with the same color block at the top
                        stacks[j].append(stacks[i].pop())
                        transfer_pairs.append((i, j))
                        break
                else:
                    # If no such stack exists, create a new stack
                    new_stack = [stacks[i].pop()]
                    stacks.append(new_stack)
                    transfer_pairs.append((i, len(stacks) - 1))
    
    # After sorting the blocks by color, move the blocks to the final stacks according to the least cost
    while True:
        total_cost = sum(costs)
        for i in range(len(stacks)):
            if stacks[i]:
                for j in range(len(stacks)):
                    if not stacks[j] or stacks[j][-1] == stacks[i][-1]:
                        heapq.heappush(transfer_pairs, (costs[i] - total_cost + costs[j], i, j))
        # If there is no block to move, break the loop
        if not transfer_pairs:
            break
        # Move the block with the least cost
        cost, i, j = heapq.heappop(transfer_pairs)
        stacks[j].append(stacks[i].pop())
        total_cost -= cost
    
    return transfer_pairs

stacks = [[], [], [], ['Red', 'Green', 'Green', 'Red'], ['Yellow', 'Blue', 'Yellow', 'Blue'], ['Yellow', 'Green', 'Red', 'Blue']]
costs = [4, 5, 5, 2, 5, 2]
print(restricted_sorting(stacks, costs))
