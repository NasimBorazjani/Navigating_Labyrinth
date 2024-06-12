
import heapq

def restricted_sorting(stacks, costs):
    # Convert the stacks into a more manageable data structure
    shades = {}
    for i, stack in enumerate(stacks):
        for shade in stack:
            if shade not in shades:
                shades[shade] = []
            shades[shade].append(i)

    # Create a priority queue to keep track of the blocks that need to be moved
    queue = []
    for i, stack in enumerate(stacks):
        if len(stack) > 0:
            shade = stack[-1]
            for j in shades[shade]:
                if j != i:
                    heapq.heappush(queue, (costs[j], i, j))

    # Move the blocks according to the rules
    transfers = []
    while queue:
        cost, src, dest = heapq.heappop(queue)
        transfers.append((src, dest))

        # Update the dictionary and the priority queue
        shade = stacks[src].pop()
        if len(stacks[src]) > 0:
            shades[stacks[src][-1]].append(src)
        else:
            shades[shade].remove(src)

        stacks[dest].append(shade)
        shades[shade].remove(dest)

        # Add the new blocks to the queue
        for i in shades[shade]:
            heapq.heappush(queue, (costs[i], src, i))

    return transfers

stacks = [[], [], ['White', 'Black', 'Green', 'White', 'Green', 'Blue'], 
          ['Red', 'Green', 'Black', 'Red', 'White', 'Yellow'], [], 
          ['Yellow', 'Black', 'Yellow', 'Red', 'Green', 'White'], [], 
          ['White', 'Blue', 'Red', 'Red', 'Blue', 'Black'], [], 
          ['Yellow', 'Blue', 'Yellow', 'Blue', 'Green', 'Black']]

costs = {0: 4, 1: 5, 2: 2, 3: 10, 4: 6, 5: 8, 6: 2, 7: 11, 8: 2, 9: 8}

print(restricted_sorting(stacks, costs))
