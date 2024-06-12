
def restricted_sorting(stacks, costs):
    transfers = []
    while any(stack for stack in stacks if len(stack) > 0):
        source_stack = max(
            (i for i, stack in enumerate(stacks) if len(stack) > 0),
            key=lambda i: len(stacks[i])
        )
        shade = stacks[source_stack][-1]
        destination_stack = max(
            (i for i, stack in enumerate(stacks) if len(stack) < 4 and (not stack or stack[-1] == shade)),
            key=lambda i: (costs[i], -len(stacks[i])) if stacks[i] else (0, 0)
        )
        transfers.append((source_stack, destination_stack))
        stacks[source_stack].pop()
        if not stacks[source_stack]:
            stacks.remove(stacks[source_stack])
        if destination_stack not in [i for i, stack in enumerate(stacks) if len(stack) < 4]:
            stacks.append([])
    return transfers

stacks = [[], ['Blue', 'Red', 'Blue', 'Red'], [], ['Green', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Blue'], []]
costs = [3, 6, 3, 2, 1, 1]
print(restricted_sorting(stacks, costs))
