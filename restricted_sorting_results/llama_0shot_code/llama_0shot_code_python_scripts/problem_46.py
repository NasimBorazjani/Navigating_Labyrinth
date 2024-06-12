
import heapq
from collections import Counter

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary
    blocks = {i: [] for i in range(8)}
    
    # Step 2: Fill the dictionary
    for i, stack in enumerate(stacks):
        for block in stack:
            blocks[i].append(block)
    
    # Step 3: Initialize the result list
    result = []
    
    # Step 4: Main loop
    while any(blocks[i] for i in range(8)):
        # Step 4a: Add all unsorted blocks to the priority queue
        queue = [(costs[i], i, color, len(blocks[i])) for i, color in enumerate(blocks) if blocks[i]]
        heapq.heapify(queue)
        
        # Step 4b: Pop the stack with the minimum cost
        _, source, target_color, _ = heapq.heappop(queue)
        
        # Step 4c: Find the target stack
        target = next((i for i, color in enumerate(blocks) if color == target_color), None)
        if target is None:
            target = len(blocks)
            blocks[target] = []
        
        # Step 4d: Move the block
        blocks[target].append(blocks[source].pop())
        
        # Step 4e: Add the move to the result
        result.append((source, target))
        
        # Step 4f: Remove the source stack if it's empty
        if not blocks[source]:
            queue = [item for item in queue if item[1] != source]
            heapq.heapify(queue)
    
    # Step 5: Return the result
    return result

# The costs of moving a block to each stack
costs = [2, 1, 6, 3, 1, 5, 4, 2]

# The initial state of the stacks
stacks = [[], [], [], ['Yellow', 'Black', 'Yellow', 'Black', 'Green'], 
          ['Red', 'Yellow', 'Blue', 'Black', 'Black'], [], 
          ['Red', 'Blue', 'Green', 'Red', 'Blue'], 
          ['Green', 'Blue', 'Red', 'Yellow', 'Green']]

print(restricted_sorting(stacks))
