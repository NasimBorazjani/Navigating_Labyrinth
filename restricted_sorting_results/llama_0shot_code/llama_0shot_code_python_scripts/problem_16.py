
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue
    queue = []
    # Initialize the transfer pairs
    transfers = []
    # Iterate over the non-empty stacks
    for i in range(len(stacks)):
        if stacks[i]:
            # Get the top block's color
            color = stacks[i][-1]
            # Iterate over the stacks again
            for j in range(len(stacks)):
                # If the stack is not full and has the same color or is empty
                if len(stacks[j]) < 3 and (stacks[j] and stacks[j][-1] == color or not stacks[j]):
                    # Calculate the cost
                    cost = costs[i] + (costs[j] if stacks[j] else 0)
                    # Add the pair to the queue
                    heapq.heappush(queue, (cost, i, j))
    # Move the blocks
    while queue:
        # Get the pair with the least cost
        cost, i, j = heapq.heappop(queue)
        # Move the block
        stacks[j].append(stacks[i].pop())
        # If the source stack is not empty
        if stacks[i]:
            # Get the top block's color
            color = stacks[i][-1]
            # Update the costs
            for k in range(len(stacks)):
                if len(stacks[k]) < 3 and (stacks[k] and stacks[k][-1] == color or not stacks[k]):
                    new_cost = costs[i] + (costs[k] if stacks[k] else 0)
                    heapq.heappush(queue, (new_cost, i, k))
        # Add the transfer pair to the result
        transfers.append((i, j))
    # Return the result
    return transfers

stacks = [['Green', 'Green', 'Blue', 'Green'], [], ['Yellow', 'Red', 'Red', 'Blue'], [], [], ['Yellow', 'Yellow', 'Blue', 'Red']]
costs = [6, 5, 2, 3, 3, 6]
print(restricted_sorting(stacks, costs))
