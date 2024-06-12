
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the stacks
    stacks = [list(reversed(stack)) for stack in stacks]
    n = len(stacks)

    # Priority queue to get the minimum cost stack
    queue = []

    # List of transfer pairs
    transfers = []

    # Iterate over each stack
    for i in range(n):
        # If the stack is not empty and has blocks of the same color in the top 3 positions
        if len(stacks[i]) > 0 and len(set(stacks[i][:3])) == 1:
            # Push the index of the stack and its cost to the priority queue
            heapq.heappush(queue, (costs[i], i))

    # Start moving the blocks
    while len(queue) > 0:
        # Pop the top item from the priority queue
        _, from_stack = heapq.heappop(queue)

        # Find the minimum cost to transfer the block
        min_cost = float('inf')
        to_stack = -1
        for i in range(n):
            if len(stacks[i]) < 4 and (len(stacks[i]) == 0 or stacks[i][-1] == stacks[from_stack][-1]):
                cost = costs[i]
                if cost < min_cost:
                    min_cost = cost
                    to_stack = i

        # Transfer the block
        stacks[to_stack].append(stacks[from_stack].pop())

        # If the 'from_stack' is not empty and has blocks of the same color in the top 3 positions
        if len(stacks[from_stack]) > 0 and len(set(stacks[from_stack][:3])) == 1:
            # Push the index of the 'from_stack' and its cost to the priority queue
            heapq.heappush(queue, (costs[from_stack], from_stack))

        # If the 'to_stack' is not empty and has blocks of the same color in the top 3 positions
        if len(stacks[to_stack]) > 0 and len(set(stacks[to_stack][:3])) == 1:
            # Push the index of the 'to_stack' and its cost to the priority queue
            heapq.heappush(queue, (costs[to_stack], to_stack))

        # Add the transfer pair to the list
        transfers.append((from_stack, to_stack))

    return transfers

stacks = [['Blue', 'Yellow', 'Red', 'Yellow'], ['Green', 'Red', 'Green', 'Red'], ['Blue', 'Green', 'Blue', 'Yellow'], [], [], []]
costs = [4, 4, 7, 7, 5, 6]
print(restricted_sorting(stacks, costs))
