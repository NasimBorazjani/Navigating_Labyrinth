
import heapq

def restricted_sorting(stacks, costs):
    need_to_move = {}
    for i, stack in enumerate(stacks):
        if len(stack) > 3:
            need_to_move[stack[-1]] = i
        if len(stack) > 1 and len(set(stack)) > 1:
            need_to_move[stack[-2]] = i
        if len(stack) > 2 and stack[-1] != stack[-2] and stack[-1] != stack[-3]:
            need_to_move[stack[-3]] = i

    heapq.heapify(need_to_move)
    result = []

    while need_to_move:
        block, from_stack = heapq.heappop(need_to_move)
        to_stack = next((i for i, stack in enumerate(stacks) if stack and stack[-1] == block), None)
        if to_stack is None:
            to_stack = len(stacks)
            stacks.append([])
        cost = min(costs[to_stack], costs[from_stack])
        result.append((from_stack, to_stack))
        stacks[from_stack].pop()
        stacks[to_stack].append(block)
        if len(stacks[from_stack]) in [2, 1]:
            heapq.heappush(need_to_move, (stacks[from_stack][-1], from_stack))
        if len(stacks[from_stack]) == 1:
            heapq.heappush(need_to_move, (stacks[from_stack][-1], from_stack))

    return result

stacks = [[], [], ['Green', 'Blue', 'Blue', 'Blue'], ['Yellow', 'Red', 'Yellow', 'Red'], ['Green', 'Red', 'Green', 'Yellow'], []]
costs = [1, 7, 2, 4, 6, 5]
print(restricted_sorting(stacks, costs))
