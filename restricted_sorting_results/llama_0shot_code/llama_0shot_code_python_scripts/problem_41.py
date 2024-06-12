
from collections import defaultdict

def restricted_sorting(stacks, costs):
    colors = defaultdict(list)
    for i, stack in enumerate(stacks):
        for color in stack:
            colors[color].append(i)

    transfers = []
    for stack in stacks:
        while len(stack) > 0:
            color = stack[-1]
            if len(colors[color]) > 1:
                src, dest = colors[color]
                if len(stacks[dest]) < 4:
                    transfers.append((src, dest))
                    stacks[dest].append(stack.pop())
                    colors[color].remove(dest)
                else:
                    for s in sorted(colors[color], key=lambda x: costs[x]):
                        if len(stacks[s]) < 4:
                            transfers.append((src, s))
                            stacks[s].append(stack.pop())
                            colors[color].remove(s)
                            break
            else:
                for s in sorted(colors.keys()):
                    if s != color and len(stacks[colors[s][0]]) < 4:
                        transfers.append((src, colors[s][0]))
                        stacks[colors[s][0]].append(stack.pop())
                        break
                else:
                    for s in sorted(range(8), key=lambda x: costs[x]):
                        if len(stacks[s]) < 4:
                            transfers.append((src, s))
                            stacks[s].append(stack.pop())
                            break

    return transfers

stacks = [['Green', 'Blue', 'Yellow', 'Green', 'Blue'], 
          ['Black', 'Green', 'Red', 'Red', 'Black'], 
          [], 
          ['Blue', 'Yellow', 'Red', 'Black', 'Yellow'], 
          [], 
          [], 
          ['Blue', 'Red', 'Black', 'Yellow', 'Green'], 
          []]

costs = [2, 1, 2, 8, 4, 3, 6, 3]

print(restricted_sorting(stacks, costs))
