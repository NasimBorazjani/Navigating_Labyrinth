
import heapq

def restricted_sorting(stacks):
    colors = {'Yellow': 0, 'Pink': 1, 'Black': 2, 'Green': 3, 'Red': 4, 'Blue': 5, 'White': 6}
    cost = [12, 11, 5, 11, 10, 9, 5, 5, 3, 10, 5, 5]
    color_count = {color: 0 for color in colors}
    color_stacks = {color: [] for color in colors}
    color_blocks = {color: 0 for color in colors}
    transfer_pairs = []
    total_cost = 0

    for i, stack in enumerate(stacks):
        for block in stack:
            color_count[block] += 1
            color_stacks[block].append(i)

    for color, count in color_count.items():
        color_blocks[color] = count * cost[colors[color]]

    heap = [(cost[i], i, stack) for i, stack in enumerate(stacks)]

    while color_blocks:
        min_cost, index, stack = heapq.heappop(heap)

        if not stack:
            continue

        block_color = stack[-1]
        to_index = color_stacks[block_color][0]
        to_stack = stacks[to_index]

        if len(to_stack) < 6 and (len(to_stack) == 0 or to_stack[-1] == block_color):
            stack.pop()
            to_stack.append(block_color)
            total_cost += min_cost
            transfer_pairs.append((index, to_index))

            if len(to_stack) == 6:
                color_stacks[block_color].pop(0)
                if not color_stacks[block_color]:
                    del color_stacks[block_color]

            if len(stack) == 0:
                heapq.heappush(heap, (cost[index], index, stack))

            color_blocks[block_color] -= min_cost
            if color_blocks[block_color] == 0:
                del color_blocks[block_color]

    return transfer_pairs, total_cost

stacks = [['Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'], ['Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'], [], [], ['Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'], ['Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'], [], [], [], [], ['Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'], ['White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink']]
transfer_pairs, total_cost = restricted_sorting(stacks)
print(transfer_pairs)
print(total_cost)
