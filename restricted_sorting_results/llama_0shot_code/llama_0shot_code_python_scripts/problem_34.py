
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the stacks that have blocks
    queue = [(-costs[i], i, stacks[i]) for i in range(len(stacks)) if stacks[i]]
    heapq.heapify(queue)

    # Initialize the dictionary to keep track of the number of blocks of each color in each stack
    colors = {}
    for i, stack in enumerate(stacks):
        if stack:
            color = stack[-1]
            if color not in colors:
                colors[color] = []
            colors[color].append(i)

    # Initialize the list of moves
    moves = []

    # Main loop
    while queue:
        cost, from_stack, to_stack = heapq.heappop(queue)

        # Find an appropriate stack to move the block to
        color = to_stack[-1]
        if color in colors and colors[color]:
            to_stack_new = colors[color].pop()
            if not colors[color]:
                del colors[color]
        else:
            to_stack_new = len(stacks)
            stacks.append([])
            colors[color] = [to_stack_new]
        cost = -cost

        # Move the block
        stacks[from_stack].pop()
        stacks[to_stack_new].append(color)
        moves.append((from_stack, to_stack_new))

        # Update the priority queue
        if stacks[from_stack]:
            color = stacks[from_stack][-1]
            heapq.heappush(queue, (-costs[from_stack]-cost, from_stack, stacks[from_stack]))

    return moves

stacks = [[], ['Yellow', 'Blue', 'Blue', 'Yellow', 'Green'], ['Black', 'Red', 'Black', 'Green', 'Red'], ['Yellow', 'Yellow', 'Red', 'Black', 'Blue'], [], ['Blue', 'Red', 'Green', 'Green', 'Black'], [], []]
costs = [6, 3, 5, 2, 8, 3, 8, 5]
print(restricted_sorting(stacks, costs))
