
import heapq

def restricted_sorting(stacks, costs):
    need_to_move = {}
    for i, stack in enumerate(stacks):
        if len(stack) > 3:
            need_to_move[stack[-1]] = i
    result = []
    while need_to_move:
        block, source = heapq.nsmallest(1, need_to_move.items(), key=lambda x: costs[x[1]])[0]
        dest = block
        while stacks[dest] and len(stacks[dest]) == 3 and stacks[dest][-1] != block:
            dest += 1
        if len(stacks[dest]) == 4:
            max_block = max(stacks[dest], key=lambda x: costs[dest])
            heapq.heappush(need_to_move, (max_block, dest))
            stacks[dest].remove(max_block)
        stacks[dest].append(block)
        result.append((source, dest))
        need_to_move.pop(block)
        if not need_to_move.get(block):
            need_to_move.pop(block)
        if len(stacks[dest]) == 3 and stacks[dest][0] == stacks[dest][1] == stacks[dest][2]:
            need_to_move.pop(stacks[dest][0])
    return result

stacks = [[], ['Blue', 'Blue', 'Green', 'Red'], [], ['Green', 'Red', 'Yellow', 'Yellow'], [], ['Green', 'Red', 'Blue', 'Yellow']]
costs = [3, 5, 1, 6, 7, 4]
print(restricted_sorting(stacks, costs))
