
import heapq

def restricted_sorting(stacks):
    # Step 1: Initialize the dictionary
    colors_count = {i: {} for i in range(8)}
    # Step 2: Update the dictionary
    for i, stack in enumerate(stacks):
        for color in stack[::-1]:
            if color in colors_count[i]:
                colors_count[i][color] += 1
            else:
                colors_count[i][color] = 1

    # Step 3: Initialize the result
    result = []

    # Step 4: While there are still blocks that need to be sorted
    while any(colors_count[i] for i in range(8)):
        # Step 4a: Find the stack with the most number of different colors of blocks
        from_stack = max(range(8), key=lambda i: len(colors_count[i]))
        # Step 4b: Find the stack with the minimum cost of accepting a block
        to_stack = min(((i, colors_count[i].get(color, 0)) for i, color in enumerate(stacks[from_stack]) if colors_count[i].get(color, 0) < 4), key=lambda x: x[0] if x[1] > 0 else float('inf'))[0]
        # Step 4c: Move the block
        result.append((from_stack, to_stack))
        # Step 4d: Update the dictionaries and the priority queue
        color = stacks[from_stack].pop()
        if color in colors_count[from_stack]:
            colors_count[from_stack][color] -= 1
        if color not in colors_count[to_stack]:
            colors_count[to_stack][color] = 1
        else:
            colors_count[to_stack][color] += 1

    # Step 5: Return the result
    return result

stacks = [[], [], ['Blue', 'Green', 'Black', 'Blue', 'Red'], ['Green', 'Red', 'Blue', 'Black', 'Blue'], [], ['Red', 'Green', 'Yellow', 'Yellow', 'Black'], ['Green', 'Black', 'Red', 'Yellow', 'Yellow'], []]
print(restricted_sorting(stacks))
