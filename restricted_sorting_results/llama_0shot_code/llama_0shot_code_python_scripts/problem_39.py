
import heapq

def restricted_sorting(stacks, costs):
    blocks = {}
    for i, stack in enumerate(stacks):
        for block in stack:
            if block not in blocks:
                blocks[block] = [0]*8
            blocks[block][i] += 1

    priority_queue = [(-count, block, i) for block, counts in blocks.items() for i, count in enumerate(counts) if count>0]
    heapq.heapify(priority_queue)

    result = []
    while priority_queue:
        count, block, src = heapq.heappop(priority_queue)
        count = -count
        dst = None
        for i in range(8):
            if i != src and (block == 'Green' and i in [0, 1, 6] or
                             block == 'Black' and i in [2, 4, 5] or
                             block == 'Blue' and i in [3, 7] or
                             block == 'Red' and i in [5, 6] or
                             block == 'Yellow' and i in [7]):
                if blocks[block][i] == 0 or (count + costs[i] < costs[src] and blocks[block][i] > 0):
                    dst = i
                    break
        if dst is None:
            dst = costs.index(min(costs[i] for i in range(8) if i != src and blocks[block][i] < 4))
        result.append((src, dst))
        blocks[block][src] -= 1
        blocks[block][dst] += 1
        if blocks[block][src] > 0:
            heapq.heappush(priority_queue, (-blocks[block][src], block, src))
    return result

stacks = [['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], []]
costs = [8, 8, 1, 2, 9, 4, 7, 8]
print(restricted_sorting(stacks, costs))
