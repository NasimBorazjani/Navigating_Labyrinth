
import heapq

def restricted_sorting(stacks):
    colors = {'Blue': 0, 'Green': 1, 'Red': 2, 'Yellow': 3, 'Black': 4}
    counts = {color: 0 for color in colors}
    color_stacks = {color: [] for color in colors}
    queue = []

    for i, stack in enumerate(stacks):
        for color in stack:
            counts[color] += 1
            color_stacks[color].append(i)

    for color, count in counts.items():
        for _ in range(count):
            for stack in color_stacks[color]:
                cost = min(stack_costs[stack], 1)
                heapq.heappush(queue, (cost, stack, color))

    transfers = []
    while queue:
        cost, from_stack, color = heapq.heappop(queue)
        to_stack = None
        for stack in color_stacks[color]:
            if stack_costs[stack] == 0 or (stack_costs[stack] > 0 and stack_colors[stack] == color):
                to_stack = stack
                break
        else:
            heapq.heappush(queue, (cost + 1, from_stack, color))
            continue

        stack_costs[from_stack] -= cost
        stack_costs[to_stack] += cost
        stack_colors[to_stack] = color
        transfers.append((from_stack, to_stack))
        counts[color] -= 1

        if counts[color] > 0:
            for stack in color_stacks[color]:
                if stack_costs[stack] == 0 or (stack_costs[stack] > 0 and stack_colors[stack] == color):
                    heapq.heappush(queue, (stack_costs[stack], stack, color))

    return transfers

stack_costs = [7, 4, 1, 2, 6, 8, 7, 6]
stack_colors = [None] * 8

initial_state = [[], ['Blue', 'Green', 'Red', 'Yellow', 'Blue'], ['Green', 'Blue', 'Yellow', 'Black', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Black', 'Black'], ['Green', 'Blue', 'Green', 'Black', 'Red'], [], []]
print(restricted_sorting(initial_state))
