
import heapq

def restricted_sorting(stacks, costs):
    # Convert the given lists into a more manageable data structure
    color_to_stacks = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in color_to_stacks:
                color_to_stacks[color] = []
            color_to_stacks[color].append(i)

    # Initialize the priority queue
    queue = []

    # Initialize the result list
    result = []

    # Iterate over each stack
    for i, stack in enumerate(stacks):
        # Sort the blocks in the stack by color
        stack.sort()

        # For each block in the stack
        for j in range(len(stack)):
            color = stack[j]

            # If the color of the block is present in other stacks
            if color in color_to_stacks and len(color_to_stacks[color]) > 1:
                # Find the stack where the block should be moved
                dest_stack = min(color_to_stacks[color], key=lambda x: costs[x] if x != i else float('inf'))

                # If the destination stack is not the current stack
                if dest_stack != i:
                    # Add a tuple to the priority queue
                    heapq.heappush(queue, (costs[dest_stack], (i, dest_stack)))

            # If the color of the block is not present in any other stack
            else:
                # Find an empty stack
                empty_stack = next((idx for idx in range(12) if idx not in color_to_stacks), None)

                # If an empty stack is found
                if empty_stack is not None:
                    # Add a tuple to the priority queue
                    heapq.heappush(queue, (costs[empty_stack], (i, empty_stack)))

            # If the current stack is empty
            if not stack:
                # Remove the color from the dictionary
                del color_to_stacks[color]
                break

    # While the priority queue is not empty
    while queue:
        # Get the tuple with the minimum cost
        _, (src, dest) = heapq.heappop(queue)

        # Add the transfer pair to the result list
        result.append((src, dest))

        # If the source stack is not empty
        if stacks[src]:
            # Move the block from the source stack to the destination stack
            color = stacks[src].pop()
            stacks[dest].append(color)

            # If the destination stack is full
            if len(stacks[dest]) == 7:
                # Remove the color from the dictionary
                del color_to_stacks[color]

            # If the source stack is empty
            if not stacks[src]:
                # Remove the color from the dictionary
                del color_to_stacks[color]

    return result

stacks = [['Black', 'Black', 'Yellow', 'Blue', 'Black', 'Black', 'Green'], [], ['Blue', 'Yellow', 'Green', 'Black', 'White', 'White', 'Blue'], ['Red', 'White', 'Pink', 'White', 'Pink', 'Green', 'Pink'], ['Green', 'Blue', 'Black', 'Green', 'Red', 'Green', 'Yellow'], [], [], ['Red', 'White', 'Blue', 'Yellow', 'Blue', 'White', 'Red'], ['Yellow', 'Yellow', 'Red', 'Pink', 'Red', 'Pink', 'Pink'], [], [], []]
costs = [10, 7, 7, 7, 9, 3, 8, 5, 4, 10, 7, 7]

print(restricted_sorting(stacks, costs))
