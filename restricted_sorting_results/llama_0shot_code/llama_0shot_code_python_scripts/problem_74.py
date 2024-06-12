
import heapq

def restricted_sorting(stacks, costs):
    # Convert the stacks into a more manageable data structure
    color_map = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in color_map:
                color_map[color] = []
            color_map[color].append(i)

    # Initialize the priority queue with the costs
    moves = []
    for i, stack in enumerate(stacks):
        for color in stack:
            if len(stack) == 1:
                continue
            for j in color_map[color]:
                if j != i and (len(stacks[j]) < 5 or stacks[j][-1] == color):
                    heapq.heappush(moves, (costs[i], i, j))

    # Apply the moves
    result = []
    while moves:
        cost, from_stack, to_stack = heapq.heappop(moves)
        if len(stacks[from_stack]) > 1:
            stacks[from_stack].pop()
            if len(stacks[to_stack]) == 0 or stacks[to_stack][-1] == stacks[from_stack][-1]:
                stacks[to_stack].append(stacks[from_stack][-1])
                result.append((from_stack, to_stack))
            else:
                heapq.heappush(moves, (cost, from_stack, to_stack))

    return result

stacks = [['Black', 'Blue', 'Red', 'White', 'Red', 'Green'], 
          ['Red', 'Black', 'Red', 'Green', 'Blue', 'Black'], 
          ['Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'], 
          [], [], 
          ['White', 'Green', 'Green', 'Red', 'Green', 'Yellow'], 
          [], 
          ['Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'], 
          [], []]

costs = [3, 8, 5, 10, 8, 2, 3, 4, 11, 3]

print(restricted_sorting(stacks, costs))
