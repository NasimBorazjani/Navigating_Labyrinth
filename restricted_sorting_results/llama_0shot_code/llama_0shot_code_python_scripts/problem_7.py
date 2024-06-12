
import heapq

def restricted_sorting(stacks):
    blocks = {}
    for i, stack in enumerate(stacks):
        for block in stack[::-1]:
            if block not in blocks:
                blocks[block] = [i]
            else:
                blocks[block].append(i)

    pq = []
    for block, stacks in blocks.items():
        target_stack = stacks[0]
        for stack in stacks[1:]:
            cost = abs(stack - target_stack) * 5
            if block == 'Yellow':
                cost += 2
            elif block == 'Green':
                cost += 3
            elif block == 'Blue':
                cost += 4
            heapq.heappush(pq, (cost, block, stack))

    result = []
    while pq:
        cost, block, source_stack = heapq.heappop(pq)
        target_stack = blocks[block].pop(0)
        result.append((source_stack, target_stack))
        if blocks[block]:
            heapq.heappush(pq, (abs(blocks[block][0] - target_stack) * 5, block, blocks[block][0]))

    return result

stacks = [[], [], [], ['Yellow', 'Green', 'Blue', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow']]
print(restricted_sorting(stacks))
