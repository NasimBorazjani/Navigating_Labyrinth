
import heapq

def restricted_sorting(stacks, costs):
    # Convert the stacks into a more manageable data structure
    color_map = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in color_map:
                color_map[color] = []
            color_map[color].append(i)

    # Create a priority queue for the blocks that need to be moved
    queue = []
    for color, stacks in color_map.items():
        if len(stacks) > 1:
            for stack in stacks:
                # Find the destination stack with the minimum cost
                dest_stack = min(stacks, key=lambda s: (costs[s], s))
                heapq.heappush(queue, (stack, dest_stack, costs[dest_stack]))

    # Move the blocks according to the queue
    transfers = []
    while queue:
        src, dest, cost = heapq.heappop(queue)
        if len(stacks[dest]) < 6:
            stacks[dest].append(stacks[src].pop())
            transfers.append((src, dest))
            # Add the block back to the queue if the destination stack is not full
            if stacks[src]:
                heapq.heappush(queue, (src, dest, cost))

    return transfers

stacks = [[], [], ['Green', 'Red', 'White', 'Green', 'Black', 'White'], [], 
          ['Red', 'Red', 'Yellow', 'White', 'Blue', 'Black'], 
          ['Blue', 'Yellow', 'Red', 'Blue', 'Blue', 'Green'], [], [], 
          ['Black', 'White', 'Black', 'White', 'Yellow', 'Blue'], 
          ['Yellow', 'Black', 'Green', 'Red', 'Green', 'Yellow']]

costs = {0: 7, 1: 11, 2: 8, 3: 10, 4: 5, 5: 6, 6: 10, 7: 10, 8: 4, 9: 11}

print(restricted_sorting(stacks, costs))
