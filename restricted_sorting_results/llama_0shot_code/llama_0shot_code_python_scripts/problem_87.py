
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary to keep track of the number of blocks of each color
    colors_count = {'Black': 0, 'Blue': 1, 'Pink': 2, 'Green': 3, 'Red': 4, 'Yellow': 5, 'White': 6}

    # Initialize the priority queue with the stacks that are not empty
    queue = []
    for i, stack in enumerate(stacks):
        if stack:
            heapq.heappush(queue, (costs[i], i, stack[-1]))

    # Initialize the empty list to store the transfer pairs
    transfer_pairs = []

    # Move the blocks until the priority queue is empty
    while queue:
        cost, src, color = heapq.heappop(queue)
        for i, stack in enumerate(stacks):
            if i != src and stack and stack[-1] == color and len(stack) < 7:
                # Move the block to the stack with the same color
                stack.append(stacks[src].pop())
                if len(stacks[src]) > 0:
                    # Push the stack back to the queue with an updated priority
                    heapq.heappush(queue, (costs[src], src, stacks[src][-1]))
                transfer_pairs.append((src, i))
                break

    return transfer_pairs

stacks = [['Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'], ['Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'], ['Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'], [], ['Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'], ['Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'], [], [], ['Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'], [], [], []]
costs = [11, 13, 4, 4, 13, 7, 12, 6, 4, 6, 11, 4]

print(restricted_sorting(stacks, costs))
