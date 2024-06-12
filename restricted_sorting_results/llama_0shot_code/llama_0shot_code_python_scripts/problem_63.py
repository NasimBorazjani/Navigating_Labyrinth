
import heapq

def restricted_sorting(stacks):
    blocks_dict = {i: stack for i, stack in enumerate(stacks)}
    costs_dict = {i: cost for i, cost in enumerate([7, 7, 8, 5, 8, 10, 5, 5, 4, 8])}
    colors_dict = {}
    for i, stack in blocks_dict.items():
        for color in stack:
            if color in colors_dict:
                colors_dict[color] += 1
            else:
                colors_dict[color] = 1
    priority_queue = [(-costs_dict[i], i) for i in blocks_dict if blocks_dict[i]]
    heapq.heapify(priority_queue)
    transfer_pairs = []
    while colors_dict:
        cost, from_stack = heapq.heappop(priority_queue)
        to_stack = None
        for i in range(len(stacks)):
            if i != from_stack and (not blocks_dict[i] or blocks_dict[i][-1] == blocks_dict[from_stack][-1]):
                to_stack = i
                break
        if to_stack is None:
            heapq.heappush(priority_queue, (-cost, from_stack))
        else:
            block = blocks_dict[from_stack].pop()
            if not blocks_dict[from_stack]:
                del blocks_dict[from_stack]
            if block in colors_dict:
                colors_dict[block] -= 1
                if not colors_dict[block]:
                    del colors_dict[block]
            if to_stack not in blocks_dict or len(blocks_dict[to_stack]) < 5:
                blocks_dict[to_stack] = blocks_dict.get(to_stack, []) + [block]
                transfer_pairs.append((from_stack, to_stack))
            else:
                heapq.heappush(priority_queue, (-cost, from_stack))
    return transfer_pairs
