
import heapq

def restricted_sorting(stacks):
    color_map = {'Red': 0, 'Yellow': 1, 'Black': 2, 'Blue': 3, 'Green': 4}
    cost_map = {0: 2, 1: 3, 2: 5, 3: 9, 4: 8, 5: 5, 6: 8, 7: 1}
    color_stack_map = {color_map[stack[-1]]: stack.pop() for stack in stacks if stack}
    empty_stacks = [[] for _ in range(8)]
    transfer_pairs = []
    total_cost = 0

    while color_stack_map:
        min_color, stack = heapq.heappop(list(color_stack_map.items()))
        if not stack:
            continue
        color = color_map[stack[-1]]
        if empty_stacks[color]:
            to_stack = empty_stacks[color]
        else:
            to_stack = [stack.pop() for _ in range(4) if stack]
            empty_stacks[color] = to_stack
        transfer_pairs.append((stack_map[id(stack)], stack_map[id(to_stack)]))
        total_cost += cost_map[min_color]
        if stack:
            heapq.heappush(color_stack_map.items(), (color_map[stack[-1]], stack))

    return transfer_pairs, total_cost

stacks = [['Red', 'Yellow', 'Red', 'Yellow', 'Black'], ['Black', 'Blue', 'Green', 'Green', 'Blue'], [], [], [], [],
          ['Black', 'Blue', 'Green', 'Black', 'Yellow'], ['Blue', 'Green', 'Yellow', 'Red', 'Red']]
stack_map = {id(stack): index for index, stack in enumerate(stacks)}
print(restricted_sorting(stacks))
