
import heapq

def restricted_sorting(stacks, costs):
    colors = {'Red': 0, 'Pink': 1, 'Green': 2, 'Blue': 3, 'White': 4, 'Yellow': 5, 'Black': 6}
    stacks = [[colors[block] for block in reversed(stack)] for stack in stacks]
    empty_stacks = [[] for _ in range(12)]
    all_stacks = stacks + empty_stacks
    heap = [(costs[i], i, stack) for i, stack in enumerate(all_stacks)]
    heapq.heapify(heap)
    result = []
    while len(heap) > 1:
        _, from_stack, blocks = heapq.heappop(heap)
        to_stack = from_stack
        while blocks:
            block = blocks.pop()
            while True:
                if to_stack // 7 in {0, 1, 2, 3, 4, 5} and len(all_stacks[to_stack]) < 6 or to_stack in {0, 1, 2, 3, 4, 5} and len(all_stacks[to_stack]) < 6 and all_stacks[to_stack][-1] == block:
                    all_stacks[to_stack].append(block)
                    break
                else:
                    _, to_stack, _ = heapq.heappop(heap)
            result.append((from_stack, to_stack))
            heapq.heappush(heap, (costs[to_stack], to_stack, all_stacks[to_stack]))
    return result

stacks = [['Red', 'Pink', 'Pink', 'Pink', 'Red', 'Black', 'Pink'], [], ['Green', 'Green', 'Blue', 'White', 'Yellow', 'Blue', 'Blue'], [], ['Green', 'Blue', 'White', 'Red', 'Blue', 'Black', 'Red'], ['Pink', 'White', 'Yellow', 'Black', 'Yellow', 'Green', 'White'], [], ['Red', 'Green', 'Black', 'White', 'Green', 'Red', 'Black'], [], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Black', 'Yellow', 'Pink'], []]
costs = {0: 10, 1: 4, 2: 5, 3: 4, 4: 7, 5: 3, 6: 11, 7: 5, 8: 9, 9: 3, 10: 11, 11: 2}
print(restricted_sorting(stacks, costs))
