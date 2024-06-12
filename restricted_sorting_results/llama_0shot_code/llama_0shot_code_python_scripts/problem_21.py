
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the stack indices and costs
    pq = [(costs[i], i) for i in range(len(stacks))]

    # List to store the transfer pairs
    transfer_pairs = []

    while True:
        # Break if all the stacks are sorted
        if all(len(stack) <= 1 or (stack[0] == stack[1] and stack[0] == stack[2]) for stack in stacks):
            break

        # Get the stack with the minimum cost
        cost, src = heapq.heappop(pq)

        # If the stack is not sorted
        if len(stacks[src]) > 1 and stacks[src][0] != stacks[src][1]:
            # Get the stack with the same color or an empty stack
            dest = next((i for i in range(len(stacks)) if i != src and (len(stacks[i]) == 0 or stacks[i][0] == stacks[src][0])), None)

            # If there is no such stack, push the src stack back to the priority queue
            if dest is None:
                heapq.heappush(pq, (cost, src))
                continue

            # Move the top block from the src stack to the dest stack
            stacks[dest].append(stacks[src].pop())

            # Add the transfer pair to the list
            transfer_pairs.append((src, dest))

            # Update the cost of the src stack
            heapq.heappush(pq, (costs[src], src))

    return transfer_pairs

stacks = [['Red', 'Yellow', 'Blue', 'Yellow'], [], [], ['Green', 'Blue', 'Green', 'Red'], [], ['Yellow', 'Red', 'Green', 'Blue']]
costs = [4, 5, 3, 3, 3, 5]
print(restricted_sorting(stacks, costs))
