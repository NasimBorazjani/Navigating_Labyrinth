
import heapq

def restricted_sorting(stacks, costs):
    # List to store the transfer pairs with their corresponding costs
    transfers = []
    
    # Priority queue to get the stack with the least cost
    queue = []
    
    # Iterate over each stack
    for i in range(len(stacks)):
        # If the stack is not empty
        if stacks[i]:
            color = stacks[i][-1]
            
            # Find the stack that can accept the block with the least cost
            for j in range(len(stacks)):
                if j != i and (not stacks[j] or stacks[j][-1] == color) and len(stacks[j]) < 3:
                    heapq.heappush(queue, (costs[j], i, j))
            
            # Move the block to the stack with the least cost
            while queue:
                cost, src, dest = heapq.heappop(queue)
                if not stacks[dest] or stacks[dest][-1] == color:
                    stacks[dest].append(stacks[src].pop())
                    transfers.append((src, dest, cost))
                    break
    
    return transfers

# Initial state of the stacks
stacks = [['Red', 'Green', 'Red', 'Blue'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Blue'], [], []]

# Cost of moving a block to the top of each stack
costs = [5, 3, 3, 1, 3, 2]

# Get the list of transfer pairs with their corresponding costs
transfers = restricted_sorting(stacks, costs)

# Print the transfer pairs in python syntax
print("[", ", ".join(f"({src}, {dest}, {cost})" for src, dest, cost in transfers), "]")
