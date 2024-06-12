
import heapq

def restricted_sorting(stacks):
    colors = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = []
            colors[color].append(i)

    pq = []
    for i, stack in enumerate(stacks):
        if stack:
            heapq.heappush(pq, (1, i))

    transfers = []
    while pq:
        cost, src = heapq.heappop(pq)
        color = stacks[src][-1]
        if colors[color]:
            dest = colors[color].pop()
            if stacks[dest]:
                heapq.heappush(pq, (1, dest))
        else:
            dest = len(stacks)
            stacks.append([])
            colors[color] = [dest]

        stacks[dest].append(stacks[src].pop())
        transfers.append((src, dest))

        if stacks[src]:
            heapq.heappush(pq, (1, src))

    return transfers

stacks = [[], ['Green', 'Blue', 'Yellow', 'Black', 'Blue'], [], [], 
          ['Blue', 'Black', 'Green', 'Yellow', 'Red'], [], 
          ['Green', 'Red', 'Black', 'Yellow', 'Blue'], 
          ['Red', 'Green', 'Red', 'Black', 'Yellow']]

print(restricted_sorting(stacks))
