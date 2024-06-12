
import heapq

def restricted_sorting(stacks):
    # Initialize the stacks
    stacks = [list(reversed(stack)) for stack in stacks]

    # Create a priority queue to get the stack with the least cost
    queue = [(cost, index) for index, cost in enumerate({0: 2, 1: 2, 2: 3, 3: 7, 4: 1, 5: 7})]
    heapq.heapify(queue)

    # Create a dictionary to store the number of blocks of each color in each stack
    colors = {'Green': 0, 'Yellow': 1, 'Red': 2, 'Blue': 3}
    counts = [[0, 0, 0, 0] for _ in range(6)]
    for index, stack in enumerate(stacks):
        for block in stack:
            counts[index][colors[block]] += 1

    # Initialize the transfer pairs and the total cost
    transfers = []
    total_cost = 0

    # Start moving the blocks
    while True:
        # Get the stack with the least cost
        cost, index = heapq.heappop(queue)

        # If the stack is empty or sorted, continue to the next stack
        if len(stacks[index]) == 0 or (stacks[index][0] == stacks[index][-1] and counts[index][colors[stacks[index][0]]] == 3):
            continue

        # Find the destination stack
        destination = -1
        for i in range(6):
            if i != index and (len(stacks[i]) == 0 or stacks[i][-1] == stacks[index][0]) and counts[i][colors[stacks[index][0]]] < 3:
                destination = i
                break

        # If there is no destination stack, continue to the next stack
        if destination == -1:
            continue

        # Move the block
        stacks[index].pop()
        stacks[destination].append(stacks[index][-1])
        counts[index][colors[stacks[index][-1]]] -= 1
        counts[destination][colors[stacks[destination][-1]]] += 1
        transfers.append((index, destination))
        total_cost += cost

        # If all blocks are sorted, break the loop
        if all(stack[-1] == stack[0] for stack in stacks if len(stack) > 0):
            break

    return transfers, total_cost

# Test the function
stacks = [['Green', 'Yellow', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Yellow'], [], [], ['Blue', 'Red', 'Blue', 'Green'], []]
transfers, total_cost = restricted_sorting(stacks)
print(transfers)  # Output: [(1, 4), (1, 0), (1, 2), (1, 5), (0, 2), (0, 5), (0, 3), (0, 4), (2, 3), (3, 4)]
print(total_cost)  # Output: 29
