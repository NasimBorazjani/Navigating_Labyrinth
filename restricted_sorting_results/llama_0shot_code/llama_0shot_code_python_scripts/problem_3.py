
import heapq

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary
    colors = {}

    # Step 2: Count the number of blocks of each color in each stack
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = {}
            if i not in colors[color]:
                colors[color][i] = 0
            colors[color][i] += 1

    # Step 3: Initialize the result list
    result = []

    # Step 4: While there is a stack with more than 3 blocks or a stack with blocks of more than one color
    while any(count > 3 or len(stack) > 1 for stack in colors.values()):
        # Step 4a: Calculate the cost of moving a block to each other stack
        costs = []
        for color in colors:
            for source in colors[color]:
                for destination in range(6):
                    if colors[color][source] > 0 and (destination not in colors or color not in colors[destination] or colors[color][destination] < 3):
                        cost = abs(source - destination) + 1
                        heapq.heappush(costs, (cost, color, source, destination))

        # Step 4b: Select the stack with the least cost
        _, color, source, destination = heapq.heappop(costs)

        # Step 4c: Move the block and update the dictionary
        colors[color][source] -= 1
        if color not in colors[destination]:
            colors[destination][color] = 0
        colors[destination][color] += 1

        # Step 4d: Append the source and destination stacks to the result list
        result.append((source, destination))

    # Step 5: Return the result list
    return result

# Test the function
stacks = [[], ['Yellow', 'Green', 'Red', 'Red'], ['Blue', 'Green', 'Red', 'Green'], ['Yellow', 'Blue', 'Yellow', 'Blue'], [], []]
print(restricted_sorting(stacks))
