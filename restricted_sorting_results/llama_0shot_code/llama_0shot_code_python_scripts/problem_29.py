
import heapq

def restricted_sorting(stacks, costs):
    # List to store the transfer pairs
    transfer_pairs = []
    
    # Priority queue to store the cost of moving a block to a stack
    # along with the index of the stack
    pq = []
    
    # Iterate over each stack
    for i in range(len(stacks)):
        # If the stack is not empty and contains blocks of more than one shade
        if stacks[i]:
            # Get the shade of the topmost block in the stack
            shade = stacks[i][-1]
            
            # Add all the stacks that accept blocks of the same shade or are empty
            # to the priority queue along with their cost
            for j in range(len(stacks)):
                if not stacks[j] or stacks[j][-1] == shade:
                    if len(stacks[j]) < 3:
                        heapq.heappush(pq, (costs[j], j))
            
            # While the stack is not empty and there are stacks in the priority queue
            while stacks[i] and pq:
                # Get the stack with the minimum cost from the priority queue
                cost, j = heapq.heappop(pq)
                
                # Move the block to the stack
                stacks[j].append(stacks[i].pop())
                
                # Add the transfer pair to the list
                transfer_pairs.append((i, j))
                
                # If the stack is not full, add it back to the priority queue
                if len(stacks[j]) < 3:
                    heapq.heappush(pq, (cost, j))
    
    return transfer_pairs

# Initial state of the stacks
stacks = [['Yellow', 'Green', 'Green', 'Blue'], [], [], ['Red', 'Green', 'Blue', 'Yellow'], [], ['Yellow', 'Blue', 'Red', 'Red']]

# Cost of moving a block to each stack
costs = [1, 5, 6, 7, 7, 5]

# Get the list of transfer pairs with the least possible cost
transfer_pairs = restricted_sorting(stacks, costs)

print(transfer_pairs)
