
import heapq

def restricted_sorting(stacks, costs):
    colors = {'Yellow': 0, 'Green': 1, 'White': 2, 'Pink': 3, 'Black': 4, 'Red': 5, 'Blue': 6}
    priority_queues = [[] for _ in range(7)]
    for i, stack in enumerate(stacks):
        while stack:
            color = colors[stack.pop()]
            heapq.heappush(priority_queues[color], (costs[i], i))
    result = []
    for color, priority_queue in enumerate(priority_queues):
        while priority_queue:
            cost, from_stack = heapq.heappop(priority_queue)
            to_stack = min((costs[i], i) for i in range(12) if not stacks[i] or colors[stacks[i][-1]] == color)
            result.append((from_stack, to_stack[1]))
            heapq.heappush(priority_queues[color], (cost - to_stack[0], from_stack))
    return result

stacks = [['Yellow', 'Green', 'White', 'Pink', 'Black', 'Pink', 'Pink'], ['Pink', 'Red', 'White', 'Black', 'Green', 'White', 'Pink'], ['Red', 'Black', 'Green', 'Blue', 'Red', 'Black', 'Yellow'], ['Blue', 'White', 'Blue', 'Blue', 'Black', 'White', 'Blue'], ['Yellow', 'Blue', 'Green', 'Green', 'Red', 'Red', 'Yellow'], [], [], [], ['Black', 'Yellow', 'Red', 'Green', 'Yellow', 'Pink', 'White'], [], [], []]
costs = [11, 11, 12, 4, 12, 2, 10, 8, 6, 10, 8, 3]
print(restricted_sorting(stacks, costs))
