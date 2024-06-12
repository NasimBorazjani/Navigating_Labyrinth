
import heapq

def restricted_sorting(stacks):
    colors = {}
    sorted_stacks = [[] for _ in range(12)]

    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = [0, []]
            colors[color][0] += 1
            colors[color][1].append(i)

    for color, (count, stack_indices) in colors.items():
        if count > 0:
            sorted_stacks[stack_indices[0]].append(color)

    queue = [(0, i) for i in range(12) if len(sorted_stacks[i]) > 1]
    heapq.heapify(queue)

    transfers = []
    total_cost = 0

    while queue:
        cost, index = heapq.heappop(queue)
        color = sorted_stacks[index].pop()
        if sorted_stacks[index]:
            heapq.heappush(queue, (costs[index], index))
        else:
            dest_index = sorted_stacks.index([color])
            heapq.heappush(queue, (costs[dest_index], dest_index))
            transfers.append((index, dest_index))
            total_cost += cost - (cost // 2)

    return transfers, total_cost

costs = {0: 10, 1: 8, 2: 6, 3: 4, 4: 11, 5: 5, 6: 11, 7: 5, 8: 7, 9: 7, 10: 10, 11: 10}
stacks = [[], ['Blue', 'Yellow', 'Pink', 'Green', 'Pink', 'Red', 'Red'], [], ['Pink', 'White', 'Pink', 'Black', 'White', 'Black', 'Pink'], ['Yellow', 'Green', 'White', 'Red', 'Yellow', 'Yellow', 'Red'], ['Green', 'Pink', 'White', 'Blue', 'Red', 'White', 'Red'], [], [], ['Blue', 'Blue', 'Yellow', 'Blue', 'Black', 'Blue', 'Green'], ['Yellow', 'Black', 'Black', 'White', 'Green', 'Green', 'Black'], [], []]

transfers, total_cost = restricted_sorting(stacks, costs)
print(f"Transfer pairs: {transfers}")
print(f"Total cost: {total_cost}")
