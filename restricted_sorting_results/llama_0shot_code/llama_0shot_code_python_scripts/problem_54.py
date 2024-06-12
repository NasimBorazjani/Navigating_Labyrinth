
import heapq

def restricted_sorting(stacks):
    colors = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = []
            colors[color].append(i)

    for color, stack_indices in colors.items():
        for i in range(len(stack_indices) - 1, 0, -1):
            heapq.heappush(stack_indices, (0, stack_indices[i]))

    costs = [8, 8, 2, 7, 9, 5, 2, 7]
    result = []

    while any(stack for stack in stacks if len(stack) > 0):
        min_cost = float('inf')
        min_stack = None
        for stack in stacks:
            if len(stack) > 0:
                cost = costs[stacks.index(stack)]
                if cost < min_cost:
                    min_cost = cost
                    min_stack = stack

        from_stack = stacks.index(min_stack)
        color = min_stack.pop()
        to_stack = next((stack for stack in stacks if len(stack) < 5 and stacks[stacks.index(stack)][-1] == color), None)

        if to_stack is None:
            to_stack = []
            stacks.append(to_stack)

        to_stack.append(color)
        result.append((from_stack, stacks.index(to_stack)))

        if len(min_stack) > 0:
            heapq.heappush(min_stack, (0, min_stack[-1]))

        if len(to_stack) < 5:
            heapq.heappush(to_stack, (0, to_stack[-1]))

    return result
