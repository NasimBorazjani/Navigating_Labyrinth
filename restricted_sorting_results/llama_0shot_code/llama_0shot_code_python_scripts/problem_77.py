
import heapq

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary to keep track of the number of blocks of each color
    colors_count = {}

    # Step 2: Iterate over the list of stacks and count the number of blocks of each color
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors_count:
                colors_count[color] = 0
            colors_count[color] += 1

    # Step 3: Initialize the priority queue with the costs to move a block to each stack
    # The cost to move a block to the stack at index i is costs[i]
    costs = [13, 5, 8, 11, 6, 9, 5, 11, 2, 11, 11, 7]
    priority_queue = [(costs[i], i, colors_count[stacks[i][-1]]) for i in range(len(stacks)) if stacks[i]]
    heapq.heapify(priority_queue)

    # Step 4: Initialize the list of stacks for each color
    colors_stacks = {color: [] for color in colors_count.keys()}
    for i, stack in enumerate(stacks):
        if stack:
            colors_stacks[stack[-1]].append(i)

    # Step 5: Initialize the dictionary where the keys are the indices of the stacks
    stacks_colors = {i: stack[-1] for i, stack in enumerate(stacks) if stack}

    # Step 6: Enter a loop where we keep moving blocks until all stacks are sorted
    moves = []
    while priority_queue:
        cost, from_stack, color_count = heapq.heappop(priority_queue)
        to_stack = None

        # Try to move the block to a stack that has the same color and it is not full
        if color_count < 6 and colors_stacks[stacks_colors[from_stack]):
            to_stack = colors_stacks[stacks_colors[from_stack]].pop()
        # If we can't find a stack that meets these conditions, move the block to the stack with the next minimum cost
        else:
            while not to_stack and priority_queue:
                _, to_stack, color_count = heapq.heappop(priority_queue)
                if color_count < 6:
                    break

        # If we can't find a stack that meets these conditions, move the block to an empty stack
        if to_stack is None:
            for i in range(len(stacks)):
                if i not in stacks_colors.keys():
                    to_stack = i
                    break

        # Update the dictionaries and the priority queue
        colors_count[stacks_colors[from_stack]] -= 1
        if colors_count[stacks_colors[from_stack]] == 0:
            del colors_stacks[stacks_colors[from_stack]]
        colors_count[stacks[to_stack][-1]] += 1
        colors_stacks[stacks[to_stack][-1]].append(to_stack)
        stacks_colors[to_stack] = stacks[to_stack][-1]

        # Store the move
        moves.append((from_stack, to_stack))

    # Step 9: Return the list of moves with the least possible cost
    return moves
