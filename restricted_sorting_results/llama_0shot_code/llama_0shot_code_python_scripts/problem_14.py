
import heapq

def restricted_sorting(stacks, costs):
    # List to store the transfer pairs
    transfer_pairs = []
    
    # Priority queue to get the stack with the least cost
    queue = []
    
    # Iterate over the non-empty stacks
    for i in range(len(stacks)):
        if stacks[i]:
            # Get the top block's color
            color = stacks[i][-1]
            
            # Get the cost of moving the block to other stacks
            for j in range(len(costs)):
                # Check if we can move the block to the corresponding stack
                if stacks[j] == [] or stacks[j][-1] == color:
                    # Check if the stack is already in the queue
                    for k in range(len(queue)):
                        if queue[k][1] == j:
                            break
                    else:
                        # Add the stack to the queue
                        heapq.heappush(queue, (costs[j], j, i))
            
            # Update the costs
            costs[i] = float('inf')
    
    # Iterate until all the blocks are sorted
    while queue:
        # Get the stack with the least cost
        cost, from_stack, to_stack = heapq.heappop(queue)
        
        # Move the block
        stacks[to_stack].append(stacks[from_stack].pop())
        
        # Add the transfer pair to the list
        transfer_pairs.append((from_stack, to_stack))
        
        # Update the costs
        for i in range(len(stacks)):
            if stacks[i]:
                color = stacks[i][-1]
                for j in range(len(costs)):
                    if stacks[j] == [] or stacks[j][-1] == color:
                        heapq.heappush(queue, (costs[j], j, i))
                costs[i] = float('inf')
    
    # Return the list of transfer pairs
    return transfer_pairs

# Test the function
stacks = [['Green', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Blue', 'Blue', 'Red'], [], ['Green', 'Green', 'Red', 'Yellow'], []]
costs = [3, 6, 5, 5, 3, 1]
print(restricted_sorting(stacks, costs))
