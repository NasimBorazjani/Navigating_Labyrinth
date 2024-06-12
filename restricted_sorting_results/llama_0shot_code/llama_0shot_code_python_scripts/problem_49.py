
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary of blocks and the priority queue
    blocks = {i: {} for i in range(8)}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color in blocks[i]:
                blocks[i][color] += 1
            else:
                blocks[i][color] = 1
        if stack:
            heapq.heappush(costs, (-costs[i], i))

    # Initialize the list of transfer pairs
    transfers = []

    # Start the loop
    while True:
        # Break the loop if all stacks are sorted
        if all(len(blocks[i]) == 1 and list(blocks[i].keys())[0] == 'Black' for i in range(8) if blocks[i]):
            break

        # Pop the stack with the highest priority
        cost, from_stack = heapq.heappop(costs)
        cost = -cost

        # If the stack is already sorted, continue to the next iteration
        if len(blocks[from_stack]) == 1:
            continue

        # Find the most expensive stack that can accept a block of the same color
        to_stack = None
        for i in range(8):
            if i != from_stack and (not blocks[i] or list(blocks[i].keys())[0] == list(blocks[from_stack].keys())[0]):
                if to_stack is None or costs[to_stack] < costs[i]:
                    to_stack = i

        # Move the block and update the dictionaries and priority queues
        color = list(blocks[from_stack].keys())[0]
        blocks[from_stack][color] -= 1
        if not blocks[from_stack]:
            heapq.heappush(costs, (float('inf'), from_stack))
        if to_stack not in blocks or blocks[to_stack][color] == 0:
            blocks[to_stack] = {color: 1}
        else:
            blocks[to_stack][color] += 1
        heapq.heappush(costs, (-costs[to_stack], to_stack))

        # Add the transfer pair to the list
        transfers.append((from_stack, to_stack))

    # Return the list of transfer pairs
    return transfers

stacks = [['Black', 'Green', 'Red', 'Yellow', 'Black'], [], ['Blue', 'Red', 'Black', 'Black', 'Yellow'], ['Green', 'Red', 'Yellow', 'Blue', 'Green'], [], [], ['Green', 'Blue', 'Red', 'Yellow', 'Blue'], []]
costs = [4, 4, 1, 9, 7, 8, 9, 7]
print(restricted_sorting(stacks, costs))
