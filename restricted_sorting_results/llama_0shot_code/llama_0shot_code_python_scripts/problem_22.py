
import heapq

def restricted_sorting(stacks, costs):
    blocks_to_move = {}
    stack_contents = {}
    for i, stack in enumerate(stacks):
        if len(stack) > 3:
            for block in stack:
                blocks_to_move[block] = i
        for block in stack:
            if block in stack_contents:
                stack_contents[block].append(i)
            else:
                stack_contents[block] = [i]

    transfer_pairs = []
    while blocks_to_move:
        block, from_stack = blocks_to_move.popitem()
        shade = block[:-1]
        if shade in stack_contents:
            to_stacks = [stack for stack in stack_contents[shade] if len(stacks[stack]) < 4]
        else:
            to_stacks = [i for i, stack in enumerate(stacks) if len(stack) < 4]
        heapq.heapify(to_stacks)
        while to_stacks:
            to_stack = heapq.heappop(to_stacks)
            if len(stacks[to_stack]) < 4 and (len(stacks[to_stack]) == 0 or stacks[to_stack][-1][:-1] == shade):
                transfer_pairs.append((from_stack, to_stack))
                if to_stack in stack_contents[shade]:
                    stack_contents[shade].remove(to_stack)
                if len(stacks[to_stack]) == 3:
                    for block in stacks[to_stack]:
                        if block in blocks_to_move:
                            del blocks_to_move[block]
                break
    return transfer_pairs

stacks = [[], ['Blue', 'Yellow', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Yellow', 'Green'], ['Green', 'Green', 'Red', 'Red']]
costs = [1, 4, 2, 7, 6, 6]
print(restricted_sorting(stacks, costs))
