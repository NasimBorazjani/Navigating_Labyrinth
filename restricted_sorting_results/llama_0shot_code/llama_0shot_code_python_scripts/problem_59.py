
from collections import defaultdict

def restricted_sorting(stacks, costs):
    colors = defaultdict(list)
    for i, stack in enumerate(stacks):
        for color in stack:
            colors[color].append(i)

    transfers = []
    for stack in stacks:
        while len(stack) > 1:
            color = stack[-1]
            if len(stack) == 5:
                target = min((c for c in colors[color] if len(stacks[c]) < 5), key=lambda c: costs[c])
            else:
                target = min((c for c in colors[color] if len(stacks[c]) < 4), key=lambda c: costs[c])
            if target != len(stacks) - 1:
                transfers.append((stacks.index(stack), target))
                stacks[target].append(stack.pop())
                colors[color].remove(target)
            else:
                transfers.append((stacks.index(stack), stacks.index(min(filter(lambda s: len(s) < 5, stacks), key=lambda s: sum(costs[i] for i in s))))
                stacks[stacks.index(min(filter(lambda s: len(s) < 5, stacks), key=lambda s: sum(costs[i] for i in s)))]
                .append(stack.pop())
                colors[color].remove(stacks.index(min(filter(lambda s: len(s) < 5, stacks), key=lambda s: sum(costs[i] for i in s))))
    return transfers

stacks = [['Green', 'Blue', 'Green', 'Yellow', 'Yellow'], [], ['Red', 'Red', 'Green', 'Black', 'Black'], [], ['Blue', 'Yellow', 'Black', 'Yellow', 'Blue'], [], [], ['Black', 'Blue', 'Red', 'Red', 'Green']]
costs = [1, 5, 5, 4, 8, 6, 8, 9]
print(restricted_sorting(stacks, costs))
