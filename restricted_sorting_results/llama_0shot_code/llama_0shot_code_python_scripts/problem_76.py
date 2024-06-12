
import heapq

def restricted_sorting(stacks, costs):
    # Step 1: Initialize a dictionary to keep track of the number of blocks of each color.
    colors_count = {}

    # Step 2: Iterate over the list of stacks and for each stack, iterate over each block.
    for i, stack in enumerate(stacks):
        for color in stack:
            # Increase the count of the corresponding color in the dictionary.
            if color in colors_count:
                colors_count[color] += 1
            else:
                colors_count[color] = 1

    # Step 3: Initialize a priority queue.
    queue = []

    # Step 4: Iterate over the dictionary and push tuples into the priority queue.
    for color, count in colors_count.items():
        for i, stack in enumerate(stacks):
            if color in stack:
                # The first element of the tuple is the cost of moving a block to a stack
                # and the second element is a tuple containing the index of the stack from
                # which a block is picked up and the color of the block.
                heapq.heappush(queue, (costs[i], (i, color)))

    # Step 5: Initialize an empty list that will contain the transfer pairs.
    transfer_pairs = []

    # Step 6: Pop elements from the priority queue and push them into the transfer pairs list.
    while queue:
        cost, (from_stack, color) = heapq.heappop(queue)
        for to_stack, stack in enumerate(stacks):
            if color not in stack or len(stack) < 6:
                transfer_pairs.append((from_stack, to_stack))
                if color in stack:
                    stack.remove(color)
                if len(stack) < 6:
                    stack.append(color)
                if len(stack) == 6:
                    break
        if all(len(stack) == 6 for stack in stacks):
            break

    # Step 7: Return the transfer pairs list.
    return transfer_pairs

stacks = [['Black', 'Blue', 'Green', 'Green', 'Pink', 'Black', 'Red'], [], ['Green', 'White', 'Yellow', 'Red', 'White', 'Blue', 'Pink'], [], [], ['Black', 'Green', 'Black', 'Yellow', 'Black', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Yellow', 'Red', 'Yellow', 'Pink'], ['Red', 'White', 'Blue', 'Pink', 'Red', 'Blue', 'White'], [], [], ['Red', 'White', 'Pink', 'Green', 'Yellow', 'White', 'Pink'], []]
costs = [7, 9, 13, 3, 4, 4, 6, 11, 12, 3, 13, 5]
print(restricted_sorting(stacks, costs))
