
import heapq

def restricted_sorting(stacks, costs):
    stack_shades = {}
    for i, stack in enumerate(stacks):
        if stack:
            stack_shades[i] = stack[-1]

    result = []
    while stack_shades:
        # Find the stack with the most number of blocks that need to be sorted
        max_stack = max(stack_shades, key=lambda x: (len(stacks[x]), stacks[x][-1]))
        shade = stack_shades[max_stack]

        # Find the empty stack or the stack with the same shade block at the top, with the minimum cost
        min_cost_stack = None
        min_cost = float('inf')
        for i in range(6):
            if not stacks[i] or stacks[i][-1] == shade:
                cost = costs[i]
                if cost < min_cost:
                    min_cost = cost
                    min_cost_stack = i

        # Move the block from the first stack to the second stack
        stacks[min_cost_stack].append(stacks[max_stack].pop())
        if not stacks[max_stack]:
            del stack_shades[max_stack]
        result.append((max_stack, min_cost_stack))

    return result

stacks = [[], [], ['Green', 'Yellow', 'Green', 'Red'], ['Green', 'Red', 'Blue', 'Yellow'], [], ['Blue', 'Red', 'Yellow', 'Blue']]
costs = [5, 1, 6, 7, 7, 7]
print(restricted_sorting(stacks, costs))
