
import heapq

def restricted_sorting(stacks):
    # Define the colors and their corresponding costs
    colors = {'Red': 0, 'Blue': 1, 'Green': 2, 'Yellow': 3}
    costs = [3, 6, 2, 4, 6, 5]

    # Initialize the priority queues for each color
    queues = {color: [] for color in colors.values()}

    # Initialize the transfer pairs list
    transfer_pairs = []

    # Iterate over each stack
    for stack_index, stack in enumerate(stacks):
        # Iterate over each block in the stack
        for block_index in range(len(stack) - 1, -1, -1):
            block = stack[block_index]
            color = colors[block]

            # Update the priority queue for the block's color
            if queues[color]:
                _, cost, dest_index = queues[color][0]
                heapq.heappush(queues[color], (cost - costs[dest_index], cost, dest_index))
            else:
                heapq.heappush(queues[color], (0, costs[stack_index], stack_index))

    # Move the blocks until all the blocks are sorted
    while any(queues[color] for color in colors.values()):
        # Find the color with the highest priority queue
        color = max(colors[block] for block in stacks if stacks[color])

        # Move the block from the stack with the highest cost to the stack with the lowest cost
        _, cost, src_index = heapq.heappop(queues[color])
        dest_index = min((costs[src_index] - cost, index) for index, (_, _, index) in enumerate(queues[color]))[1]
        heapq.heappush(queues[color], (costs[dest_index] - cost, cost, dest_index))
        transfer_pairs.append((src_index, dest_index))

    # Return the transfer pairs with their corresponding costs
    return transfer_pairs

# Test the function
stacks = [['Red', 'Blue', 'Green', 'Yellow'], ['Blue', 'Blue', 'Green', 'Red'], [], [], [], ['Green', 'Red', 'Yellow', 'Yellow']]
print(restricted_sorting(stacks))
