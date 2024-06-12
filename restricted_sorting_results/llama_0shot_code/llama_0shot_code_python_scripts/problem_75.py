
import heapq

def restricted_sorting(stacks, costs):
    color_to_num = {'White': 0, 'Black': 1, 'Red': 2, 'Green': 3, 'Blue': 4, 'Yellow': 5}
    num_to_color = {v: k for k, v in color_to_num.items()}
    stacks = [[color_to_num[color] for color in stack] for stack in stacks]
    heap = [(cost, i, j) for i, cost in enumerate(costs)]
    heapq.heapify(heap)
    result = []
    while True:
        cost, src, dest = heapq.heappop(heap)
        if stacks[src]:
            block = stacks[src].pop()
            if stacks[dest] and stacks[dest][-1] != block:
                heapq.heappush(heap, (costs[stacks[dest].index(block)], stacks[dest].index(block), dest))
                stacks[dest].remove(block)
            else:
                stacks[dest].append(block)
            result.append((src, dest))
        if all(len(stack) == 5 and len(set(stack)) == 1 for stack in stacks):
            break
    return [(num_to_color[src], num_to_color[dest]) for src, dest in result]

stacks = [['White', 'Green', 'Red', 'Blue', 'Red', 'Yellow'], 
          ['Black', 'Black', 'White', 'Blue', 'Green', 'Green'], 
          ['White', 'Blue', 'White', 'Yellow', 'Black', 'Green'], 
          [], [], [], [], 
          ['Green', 'Yellow', 'Red', 'White', 'Blue', 'Black'], 
          ['Yellow', 'Red', 'Blue', 'Red', 'Black', 'Yellow'], []]

costs = [8, 8, 10, 6, 8, 4, 3, 7, 11, 9]

print(restricted_sorting(stacks, costs))
