
import heapq

def restricted_sorting(stacks):
    # Initialize the stacks
    stacks = [list(reversed(s)) for s in stacks]
    # Initialize the priority queue
    queue = [(0, i) for i in range(len(stacks))]
    heapq.heapify(queue)
    # Initialize the dictionary to keep track of the number of blocks in each shade
    shades = {}
    for i, stack in enumerate(stacks):
        if stack:
            shades[stack[-1]] = shades.get(stack[-1], []) + [i]
    # Initialize the list of transfer pairs
    transfers = []
    # Move the blocks
    while True:
        # Get the stack with the minimum cost
        cost, src = heapq.heappop(queue)
        if not stacks[src]:
            continue
        shade = stacks[src].pop()
        if shades.get(shade, []):
            dst = shades[shade].pop()
            if len(stacks[dst]) < 3:
                stacks[dst].append(shade)
                transfers.append((src, dst))
                heapq.heappush(queue, (cost - 1, src))
                continue
        # Move the block to the stack with the minimum cost
        for _ in range(2):
            heapq.heappush(queue, (cost - 1, src))
        for _ in range(3):
            heapq.heappush(queue, (0, src))
    return transfers

# Test the function
stacks = [['Blue', 'Red', 'Green', 'Yellow'], [], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Blue', 'Blue', 'Green', 'Red'], []]
shades = ['Blue', 'Red', 'Green', 'Yellow']
costs = [2, 3, 3, 6, 1, 6]
stacks = [[s for s in shades if s in stack] for stack in stacks]
print(restricted_sorting(stacks))
