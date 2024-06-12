
import heapq

def restricted_sorting(stacks):
    colors = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = []
            colors[color].append(i)

    costs = [4, 6, 8, 2, 4, 7, 7, 5]
    priority_queue = [(costs[i], i) for i in range(len(stacks)) if stacks[i]]
    heapq.heapify(priority_queue)

    result = []
    while any(stack for stack in stacks if stack):
        cost, source = heapq.heappop(priority_queue)
        color = stacks[source][-1]
        targets = colors[color]
        while True:
            if not targets or len(stacks[targets[0]]) == 5 or (stacks[targets[0]] and stacks[targets[0]][-1] != color):
                targets.pop(0)
            else:
                target = targets[0]
                break
        heapq.heappush(priority_queue, (costs[target], target))
        result.append((source, target))
        stacks[source].pop()
        if stacks[source]:
            heapq.heappush(priority_queue, (costs[source], source))
        stacks[target].append(color)
    return result

stacks = [[], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green']]
print(restricted_sorting(stacks))
