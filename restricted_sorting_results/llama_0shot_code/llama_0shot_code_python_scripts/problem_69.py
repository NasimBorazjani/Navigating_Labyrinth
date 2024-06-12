
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue and the lists to keep track of the number of blocks and the color of the top block in each stack
    queue = []
    num_blocks = [len(stack) for stack in stacks]
    top_blocks = [stack[-1] if stack else None for stack in stacks]

    # Iterate over each stack
    for i in range(len(stacks)):
        # If the stack is not empty
        if num_blocks[i] > 0:
            # Pop a block from it
            num_blocks[i] -= 1
            color = top_blocks[i]
            top_blocks[i] = stacks[i][-1] if len(stacks[i]) > 1 else None

            # Calculate the cost of moving this block to each other stack
            for j in range(len(stacks)):
                if (num_blocks[j] < 6 and top_blocks[j] == color) or top_blocks[j] is None:
                    heapq.heappush(queue, (costs[j], i, j))

    # Initialize the list of transfer pairs
    transfer_pairs = []

    # Repeat the process until the priority queue is empty or all the blocks are sorted
    while queue and not all(num_block == 0 for num_block in num_blocks):
        # Pop a tuple from the priority queue
        _, from_stack, to_stack = heapq.heappop(queue)

        # If the 'to' stack is not full and has the same color as the block or is empty
        if num_blocks[to_stack] < 6 and (top_blocks[to_stack] == top_blocks[from_stack] or top_blocks[to_stack] is None):
            # Move the block
            num_blocks[from_stack] -= 1
            num_blocks[to_stack] += 1
            top_blocks[from_stack] = stacks[from_stack][-1] if len(stacks[from_stack]) > 1 else None
            top_blocks[to_stack] = top_blocks[from_stack]

            # Add the transfer pair to the list
            transfer_pairs.append((from_stack, to_stack))

    return transfer_pairs

# Test the function
stacks = [[], ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'], ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'], [], ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'White', 'White', 'Red', 'White', 'Black'], [], ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'], [], []]
costs = [5, 4, 7, 7, 11, 11, 8, 3, 7, 9]
print(restricted_sorting(stacks, costs))
