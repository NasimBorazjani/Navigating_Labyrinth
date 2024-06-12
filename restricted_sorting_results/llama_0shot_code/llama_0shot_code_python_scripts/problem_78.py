
import heapq

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary to keep track of the number of blocks of each color
    colors = {}

    # Step 2: Iterate over the initial state of the stacks
    for i, stack in enumerate(stacks):
        # Count the number of blocks of each color and update the dictionary
        for block in stack:
            if block in colors:
                colors[block].append(i)
            else:
                colors[block] = [i]

    # Step 3: Initialize the priority queue with the costs of moving a block to a stack
    queue = [(costs[i], i, color) for i, color in enumerate(colors)]
    heapq.heapify(queue)

    # Step 4: Initialize an empty list to store the transfer pairs
    transfer_pairs = []

    # Step 5: Iterate over the colors
    for color in colors:
        while len(colors[color]) > 1:
            # Pop the top block from the stack with the most number of blocks of that color
            max_stack = colors[color].pop()

            # Push it to the stack with the minimum cost
            min_cost, min_stack, min_color = heapq.heappop(queue)
            while min_color != color or len(colors[min_color]) == 6:
                heapq.heappush(queue, (min_cost, min_stack, min_color))
                min_cost, min_stack, min_color = heapq.heappop(queue)

            heapq.heappush(queue, (min_cost, min_stack, min_color))
            transfer_pairs.append((max_stack, min_stack))

    # Step 6: Repeat step 5 until all the blocks are sorted
    while queue:
        min_cost, min_stack, min_color = heapq.heappop(queue)
        while len(colors[min_color]) < 6:
            # Pop the top block from the stack with the most number of blocks of that color
            max_stack = colors[min_color].pop()

            # Push it to the stack with the minimum cost
            transfer_pairs.append((max_stack, min_stack))

    # Step 7: Return the list of transfer pairs
    return transfer_pairs

costs = {0: 2, 1: 7, 2: 5, 3: 11, 4: 6, 5: 13, 6: 12, 7: 7, 8: 8, 9: 6, 10: 7, 11: 7}
stacks = [[], ['Blue', 'Pink', 'Red', 'Red', 'Yellow', 'White', 'Green'], [], [], ['White', 'Black', 'Blue', 'Yellow', 'Yellow', 'Pink', 'White'], ['Green', 'Pink', 'White', 'Blue', 'Pink', 'Red', 'Pink'], ['Black', 'Green', 'Yellow', 'White', 'Yellow', 'Red', 'Blue'], [], ['Red', 'White', 'Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Green', 'Black', 'Pink', 'Black', 'Red', 'Green', 'Blue'], []]
print(restricted_sorting(stacks))
