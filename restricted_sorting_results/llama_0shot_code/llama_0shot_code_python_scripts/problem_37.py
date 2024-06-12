
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

    costs = [3, 2, 1, 7, 5, 5, 6, 4]
    queue = []
    result = []

    while any(stack for stack in stacks if len(stack) > 0):
        for color, stack_indices in colors.items():
            while stack_indices:
                cost, index = heapq.heappop(stack_indices)
                if cost == 0:
                    break
                heapq.heappush(queue, (cost + costs[index], index))

        while queue:
            cost, from_index = heapq.heappop(queue)
            to_index = -1
            for color, stack_indices in colors.items():
                if stack_indices and stack_indices[0] == 0:
                    to_index = stack_indices[1]
                    break

            if to_index == -1:
                to_index = len(stacks)
                stacks.append([])
                colors[color].append(to_index)
                heapq.heappush(stack_indices, (0, to_index))

            stacks[from_index].pop()
            stacks[to_index].append(color)
            result.append((from_index, to_index))

            if len(stacks[from_index]) > 0:
                heapq.heappush(queue, (costs[from_index] + 1, from_index))

            break

    return result
