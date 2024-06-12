
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionaries and the priority queue
    stack_colors = {i: [] for i in range(10)}
    color_stacks = {i: [] for i in range(10)}
    for i, stack in enumerate(stacks):
        if stack:
            color = stack[-1]
            stack_colors[i] = color
            heapq.heappush(color_stacks[color], (costs[i], i))

    # Move the blocks
    transfers = []
    while color_stacks:
        color, (cost, src) = heapq.heappop(color_stacks[stack_colors[src]])
        if color_stacks[color]:
            dst = color_stacks[color][0][1]
        else:
            dst = len(stacks)
            stacks.append([])
            color_stacks[color] = [(costs[dst], dst)]
            heapq.heapify(color_stacks[color])
        transfers.append((src, dst))
        stacks[dst].append(stacks[src].pop())
        if not stacks[src]:
            del stack_colors[src]
            for color in color_stacks:
                color_stacks[color] = [x for x in color_stacks[color] if x[1] != src]
                if color_stacks[color]:
                    heapq.heapify(color_stacks[color])
                else:
                    del color_stacks[color]
    return transfers

stacks = [[], [], ['White', 'Yellow', 'Yellow', 'Green', 'Blue', 'Green'], 
          ['Red', 'Yellow', 'White', 'Blue', 'Black', 'Black'], 
          ['Black', 'Red', 'Blue', 'Black', 'Green', 'Green'], 
          ['Green', 'Black', 'Yellow', 'Red', 'White', 'Red'], 
          ['White', 'Blue', 'Red', 'Blue', 'White', 'Yellow'], [], [], []]

costs = {0: 4, 1: 1, 2: 1, 3: 9, 4: 2, 5: 9, 6: 1, 7: 9, 8: 6, 9: 4}

print(restricted_sorting(stacks, costs))
