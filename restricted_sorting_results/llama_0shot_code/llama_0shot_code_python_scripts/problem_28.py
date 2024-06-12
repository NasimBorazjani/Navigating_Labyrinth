
import heapq

def restricted_sorting(stacks):
    # Initialize the stacks
    stacks = [list(reversed(s)) for s in stacks]
    n = len(stacks)

    # Create a priority queue to get the minimum cost stack
    queue = [(-len(s), i) for i, s in enumerate(stacks) if s]
    heapq.heapify(queue)

    # Create a dictionary to keep track of the number of blocks in each shade
    shades = {}
    for s in stacks:
        for b in s:
            shades[b] = shades.get(b, 0) + 1

    # Initialize the transfer pairs
    transfers = []

    # Move the blocks
    costs = [3, 7, 7, 7, 2, 4]
    while queue:
        cost, src = heapq.heappop(queue)
        src_shade = stacks[src][-1]
        if not stacks[src]:
            continue
        stacks[src].pop()
        cost = -cost
        if not stacks[src]:
            heapq.heappush(queue, (cost, src))
        else:
            heapq.heappush(queue, (cost - 1, src))
        if not shades[src_shade]:
            continue
        shades[src_shade] -= 1
        dest = None
        for i in range(n):
            if not stacks[i] or stacks[i][-1] == src_shade:
                dest = i
                break
        if dest is None:
            dest = n
            for i in range(n):
                if not stacks[i]:
                    dest = i
                    break
        if not stacks[dest]:
            heapq.heappush(queue, (costs[dest], dest))
        else:
            heapq.heappush(queue, (costs[dest] - 1, dest))
        stacks[dest].append(src_shade)
        transfers.append((src, dest))

    return transfers

stacks = [['Green', 'Yellow', 'Red', 'Red'], [], ['Yellow', 'Green', 'Blue', 'Yellow'], [], [], ['Red', 'Blue', 'Green', 'Blue']]
shades = ['Green', 'Yellow', 'Red', 'Blue']
print(restricted_sorting(stacks))
