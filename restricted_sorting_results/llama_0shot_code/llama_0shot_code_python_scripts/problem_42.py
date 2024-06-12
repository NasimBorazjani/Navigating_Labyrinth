
import heapq

def restricted_sorting(stacks, costs):
    blocks = {}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in blocks:
                blocks[block] = [0]*8
            blocks[block][i] += 1

    priority_queue = []
    for block, counts in blocks.items():
        heapq.heappush(priority_queue, (counts[0], block, 0))

    result = []
    while priority_queue:
        count, block, src = heapq.heappop(priority_queue)
        if count == 0:
            break
        dest, cost = min(((i, costs[i]) for i in range(8) if stacks[i] < 5 and (not stacks[i] or stacks[i][-1] == block)), key=lambda x: x[1])
        result.append((src, dest))
        stacks[dest].append(block)
        blocks[block][src] -= 1
        if blocks[block][src] > 0:
            heapq.heappush(priority_queue, (blocks[block][src], block, src))
        stacks[src] = stacks[src][1:] if stacks[src] else []

    return result

stacks = [['Blue', 'Black', 'Yellow', 'Black', 'Red'], ['Blue', 'Blue', 'Green', 'Black', 'Yellow'], [], ['Yellow', 'Red', 'Red', 'Green', 'Green'], [], [], ['Red', 'Blue', 'Black', 'Green', 'Yellow'], []]
costs = [7, 5, 7, 2, 6, 7, 5, 3]
print(restricted_sorting(stacks, costs))
