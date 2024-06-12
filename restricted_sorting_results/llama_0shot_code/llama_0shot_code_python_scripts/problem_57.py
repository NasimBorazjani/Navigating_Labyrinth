
import heapq

def restricted_sorting(stacks, costs):
    # Step 1: Initialize the dictionary
    colors = {}
    
    # Step 2: Update the dictionary
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = [0]*8
            colors[color][i] += 1

    # Step 3: Initialize the result
    result = []
    
    # Step 4: While there are unsorted blocks
    while any(any(value > 0 for value in color) for color in colors.values()):
        # Step 4a: Add all unsorted blocks to the priority queue
        queue = []
        for color, counts in colors.items():
            for i, count in enumerate(counts):
                if count > 0:
                    heapq.heappush(queue, (costs[i], i, color))
        
        # Step 4b: Pop the stack with the minimum cost
        _, src, _ = heapq.heappop(queue)
        
        # Step 4c: Find the most common color
        target_color = max(colors, key=lambda color: sum(colors[color]))
        target_count = sum(colors[target_color])
        
        # Step 4d: Try to move the block
        if colors[target_color][src] > 0 or all(count == 0 for count in colors[target_color]):
            colors[target_color][src] -= 1
            result.append((src, colors[target_color].index(max(colors[target_color]))))
        else:
            # Step 4e: Add the cost of moving the block to the priority queue
            target = colors[target_color].index(max(colors[target_color]))
            heapq.heappush(queue, (costs[src] + costs[target], src, target_color))
    
    # Step 5: Return the result
    return result

stacks = [[], [], ['Green', 'Red', 'Black', 'Blue', 'Blue'], ['Yellow', 'Blue', 'Blue', 'Green', 'Black'], ['Yellow', 'Yellow', 'Yellow', 'Red', 'Black'], [], [], ['Red', 'Green', 'Green', 'Red', 'Black']]
costs = [2, 3, 9, 8, 3, 7, 9, 5]
print(restricted_sorting(stacks, costs))
