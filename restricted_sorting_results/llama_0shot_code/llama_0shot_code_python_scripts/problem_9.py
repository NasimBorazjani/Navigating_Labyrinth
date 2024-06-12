
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the stacks
    stacks = [list(reversed(stack)) for stack in stacks]
    shades = ['Yellow', 'Red', 'Blue', 'Green']
    num_blocks = {shade: 0 for shade in shades}
    for stack in stacks:
        for block in stack:
            num_blocks[block] += 1

    # Initialize the priority queue
    queue = [(-cost, index) for index, cost in enumerate(costs)]
    heapq.heapify(queue)

    # Initialize the transfer pairs
    transfer_pairs = []

    # Iterate over each stack
    for i, stack in enumerate(stacks):
        while stack:
            # Get the minimum cost stack
            cost, j = heapq.heappop(queue)

            # Move the block to the appropriate stack
            block = stack.pop()
            transfer_pairs.append((i, j))
            num_blocks[block] -= 1

            # If the stack is not full, add it back to the queue
            if len(stacks[j]) < 3:
                heapq.heappush(queue, (cost, j))

    return transfer_pairs

# Test the function
stacks = [['Yellow', 'Yellow', 'Red', 'Red'], [], ['Blue', 'Yellow', 'Red', 'Green'], [], ['Green', 'Blue', 'Green', 'Blue'], []]
costs = [7, 1, 4, 7, 4, 4]
print(restricted_sorting(stacks, costs))
