
import heapq

def restricted_sorting(stacks, costs):
    color_map = {}
    for i, stack in enumerate(stacks):
        for color in set(stack):
            if color not in color_map:
                color_map[color] = []
            color_map[color].append(i)

    result = []
    for stack_index, stack in enumerate(stacks):
        while len(stack) > 1:
            color = stack[-1]
            possible_stacks = color_map[color]
            possible_stacks.remove(stack_index)
            heap = [(costs[j] if j not in possible_stacks else float('inf'), j) for j in range(len(stacks))]
            heapq.heapify(heap)
            while True:
                cost, index = heapq.heappop(heap)
                if cost != float('inf'):
                    result.append((stack_index, index))
                    stack.pop()
                    break

    return result

stacks = [['Red', 'Red', 'Red', 'Green', 'Yellow'], ['Black', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], [], ['Black', 'Blue', 'Black', 'Yellow', 'Green'], [], ['Blue', 'Green', 'Blue', 'Black', 'Blue']]
costs = [8, 2, 7, 6, 7, 1, 5, 3]
print(restricted_sorting(stacks, costs))
