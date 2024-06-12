
import heapq

def restricted_sorting(stacks, costs):
    color_map = {'Red': 0, 'Black': 1, 'Yellow': 2, 'White': 3, 'Blue': 4, 'Green': 5, 'Pink': 6}
    stacks = [[(color_map[color], 1) for color in reversed(stack)] for stack in stacks]
    sorted_stacks = [[] for _ in range(len(stacks))]
    moves = []
    for from_stack, stack in enumerate(stacks):
        for color, count in stack:
            if not sorted_stacks[color]:
                moves.append((from_stack, color, count, costs[color]))
            else:
                sorted_stacks[color].append((color, count))
    while moves:
        from_stack, color, count, cost = heapq.heappop(moves)
        if not sorted_stacks[color] or sorted_stacks[color][-1][0] == color:
            sorted_stacks[color].append((color, count))
            if len(sorted_stacks[color]) == 6:
                sorted_stacks[color] = sorted(sorted_stacks[color], key=lambda x: x[0])
        else:
            heapq.heappush(moves, (from_stack, color, count, cost))
    return sorted_stacks

stacks = [['Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'], [], ['White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'], ['Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'], [], ['Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'], ['Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'], ['Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'], [], [], [], []]
costs = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}
print(restricted_sorting(stacks, costs))
