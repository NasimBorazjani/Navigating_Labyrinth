
import heapq

def restricted_sorting(stacks):
    colors = {'Green': 0, 'Yellow': 1, 'Red': 2, 'Blue': 3, 'Black': 4}
    costs = [4, 8, 9, 9, 5, 7, 9, 6]
    block_counts = {color: 0 for color in colors}
    color_stacks = {color: [] for color in colors}
    pq = []

    for i, blocks in enumerate(stacks):
        if blocks:
            color = blocks[-1]
            block_counts[color] += len(blocks)
            color_stacks[color].append(i)
            heapq.heappush(pq, (costs[i], i))

    transfers = []
    while block_counts[max(block_counts, key=block_counts.get)] > 4:
        cost, from_stack = heapq.heappop(pq)
        to_stack = None

        if block_counts[colors[stacks[from_stack][-1]]] < 4:
            to_stack = color_stacks[colors[stacks[from_stack][-1]]].pop()
        else:
            min_cost = float('inf')
            for color in colors:
                if color != colors[stacks[from_stack][-1]] and block_counts[color] < 4:
                    min_cost = min(min_cost, costs[color_stacks[color][0]])
            if min_cost < float('inf'):
                for color in colors:
                    if costs[color_stacks[color][0]] == min_cost:
                        to_stack = color_stacks[color].pop()
                        break

        if to_stack is not None:
            transfers.append((from_stack, to_stack))
            block_counts[colors[stacks[from_stack][-1]]] -= 1
            block_counts[colors[stacks[to_stack][-1]]] += 1
            heapq.heappush(pq, (costs[from_stack], from_stack))

    return transfers

stacks = [[], ['Green', 'Yellow', 'Red', 'Red', 'Red'], [], ['Green', 'Yellow', 'Green', 'Blue', 'Black'], 
          ['Red', 'Yellow', 'Black', 'Blue', 'Black'], [], [], ['Green', 'Black', 'Yellow', 'Blue', 'Blue']]
print(restricted_sorting(stacks))
