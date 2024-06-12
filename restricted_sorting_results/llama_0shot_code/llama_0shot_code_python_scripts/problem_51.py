
import heapq

def restricted_sorting(stacks, costs):
    color_counts = {}
    for stack in stacks:
        for color in stack:
            if color in color_counts:
                color_counts[color] += 1
            else:
                color_counts[color] = 1

    max_color = max(color_counts, key=color_counts.get)
    min_cost_heap = [(costs[i], i, color_counts[stacks[i][-1]] if stacks[i] else 0) for i in range(len(stacks))]
    heapq.heapify(min_cost_heap)
    transfer_pairs = []

    while color_counts[max_color] < 4:
        cost, from_stack, count = heapq.heappop(min_cost_heap)
        if stacks[from_stack] and stacks[from_stack][-1] != max_color:
            to_stack = next((i for i in range(len(stacks)) if not stacks[i] or stacks[i][-1] == max_color), None)
            if to_stack is not None:
                transfer_pairs.append((from_stack, to_stack))
                if len(stacks[from_stack]) == 1:
                    del stacks[from_stack]
                    heapq.heappush(min_cost_heap, (costs[from_stack], from_stack, 0))
                else:
                    stacks[from_stack].pop()
                    heapq.heappush(min_cost_heap, (costs[from_stack], from_stack, count - 1))
        else:
            heapq.heappush(min_cost_heap, (cost, from_stack, count))
        color_counts = {color: count for color, count in color_counts.items() if count > 0}
        max_color = max(color_counts, key=color_counts.get)

    return transfer_pairs

stacks = [[], [], [], ['Green', 'Blue', 'Blue', 'Green', 'Black'], ['Red', 'Green', 'Blue', 'Blue', 'Red'], ['Black', 'Black', 'Yellow', 'Red', 'Yellow'], [], ['Yellow', 'Black', 'Green', 'Red', 'Yellow']]
costs = [7, 8, 2, 8, 9, 6, 8, 1]
print(restricted_sorting(stacks, costs))
