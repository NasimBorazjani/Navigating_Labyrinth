
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary to keep track of the blocks in each stack
    blocks = {i: [] for i in range(8)}
    # Initialize the priority queue to keep track of the stacks with the minimum cost
    queue = []
    # Iterate over the given initial state of the stacks
    for i, stack in enumerate(stacks):
        # Add the blocks to the dictionary
        blocks[i] = stack
        # If the stack is not empty, add the stack to the priority queue with its cost as the priority
        if stack:
            heapq.heappush(queue, (costs[i], i))
    # Initialize the list of transfer pairs
    transfers = []
    # Move the blocks
    for color, stack in sorted(blocks.items()):
        while stack:
            # Pop the stack with the minimum cost from the priority queue
            cost, dest = heapq.heappop(queue)
            # Add the block to the destination stack
            blocks[dest].append(stack.pop())
            # If the destination stack becomes full, remove it from the priority queue
            if len(blocks[dest]) < 4:
                heapq.heappush(queue, (costs[dest], dest))
            # Add the transfer pair to the list
            transfers.append((color, dest))
    # Return the list of transfer pairs with their corresponding costs
    return transfers

stacks = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], 
          ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], 
          ['Green', 'Red', 'Black', 'Yellow', 'Blue'], 
          ['Red', 'Green', 'Red', 'Black', 'Yellow']]

costs = [2, 4, 5, 2, 2, 3, 2, 5]

print(restricted_sorting(stacks, costs))
