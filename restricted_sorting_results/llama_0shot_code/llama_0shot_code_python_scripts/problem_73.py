
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the dictionary of blocks and the priority queue
    blocks = {color: [] for color in set(sum(stacks, []))}
    for i, stack in enumerate(stacks):
        if stack:
            color = stack[-1]
            blocks[color].append(i)
            heapq.heappush(stacks, (costs[i], i, stack))

    # Initialize the list of transfer pairs
    transfers = []

    # Start the loop
    while True:
        # Pop a stack from the priority queue
        _, src, stack = heapq.heappop(stacks)

        # If the stack is empty, continue to the next iteration
        if not stack:
            continue

        # Get the color of the top block
        color = stack[-1]

        # Try to find an appropriate stack
        for _ in range(len(stacks)):
            _, dst, _ = heapq.heappop(stacks)
            if len(stacks[dst]) < 5 and (not stacks[dst] or stacks[dst][-1] == color):
                # Move the block and update the dictionaries and lists
                stacks[dst].append(stack.pop())
                blocks[color].remove(src)
                if not stack:
                    blocks[color].remove(dst)
                transfers.append((src, dst))
                break
            else:
                heapq.heappush(stacks, (costs[dst], dst, stacks[dst]))

        # If all the stacks are sorted, return the list of transfer pairs
        if all(len(stack) == 5 for stack in stacks if stack):
            return transfers

        # Update the priorities of the stacks
        for i in range(len(stacks)):
            _, src, stack = stacks[i]
            if stack:
                heapq.heappush(stacks, (costs[src], src, stack))
