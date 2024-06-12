
import heapq

def restricted_sorting(stacks, costs):
    # Step 1: Initialize a dictionary to keep track of the number of blocks of each color
    colors_count = {}

    # Step 2: Iterate over the list of stacks and count the number of blocks of each color
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in colors_count:
                colors_count[block] = [0, []]
            colors_count[block][0] += 1
            colors_count[block][1].append(i)

    # Step 3: Initialize a priority queue
    queue = []

    # Step 4: Iterate over the dictionary and calculate the cost of moving all the blocks of each color
    for color, (count, stack_indices) in colors_count.items():
        for stack_index in stack_indices:
            for other_stack_index in range(12):
                if other_stack_index not in stack_indices:
                    heapq.heappush(queue, (costs[other_stack_index], (stack_index, other_stack_index)))

    # Step 5: Pop elements from the priority queue and add them to the result list
    result = []
    while sum(colors_count[color][0] for color in colors_count) > 0:
        cost, (from_stack, to_stack) = heapq.heappop(queue)
        colors_count[stacks[from_stack][-1]][0] -= 1
        if colors_count[stacks[from_stack][-1]][0] == 0:
            del colors_count[stacks[from_stack][-1]]
        stacks[from_stack].pop()
        if stacks[to_stack]:
            stacks[to_stack][-1] = color
        else:
            stacks[to_stack].append(color)
        result.append((from_stack, to_stack))

    return result

stacks = [['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'], [], [], ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'], [], ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'], ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'], ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'], [], ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'], [], []]
costs = [2, 7, 2, 2, 4, 13, 4, 6, 8, 6, 10, 10]
print(restricted_sorting(stacks, costs))
