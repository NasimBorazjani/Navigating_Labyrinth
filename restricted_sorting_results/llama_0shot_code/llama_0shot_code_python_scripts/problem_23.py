
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the stacks and costs
    stacks = [list(reversed(stack)) for stack in stacks]
    costs = list(map(list, zip(*costs)))

    # Initialize the result list
    result = []

    # Iterate over each stack
    for i in range(len(stacks)):
        # If the stack is not empty
        if stacks[i]:
            # Pop out the top block
            block = stacks[i].pop()

            # Find the best destination stack
            q = [(costs[j][block], j) for j in range(len(costs)) if not stacks[j] or stacks[j][-1] == block]
            _, dest = heapq.heappop(q)

            # Add the transfer pair to the result list
            result.append((i, dest))

            # Update the stacks and costs
            stacks[dest].append(block)
            costs[i][block] = max(costs[i][block] - 1, 1)

    return result

stacks = [['Green', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Yellow', 'Blue'], [], ['Green', 'Yellow', 'Red', 'Yellow'], [], []]
costs = [[2, 7, 4, 7, 6, 3], [2, 7, 4, 7, 6, 3], [2, 7, 4, 7, 6, 3], [2, 7, 4, 7, 6, 3], [2, 7, 4, 7, 6, 3], [2, 7, 4, 7, 6, 3]]

print(restricted_sorting(stacks, costs))
