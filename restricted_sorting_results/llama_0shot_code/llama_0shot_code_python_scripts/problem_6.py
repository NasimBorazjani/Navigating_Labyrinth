
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the costs
    pq = [(-costs[i], i, stacks[i]) for i in range(len(stacks))]
    heapq.heapify(pq)

    # List to store the transfer pairs
    transfer_pairs = []

    while len(pq) > 1:
        # Pop the stack with the minimum cost
        cost, src, blocks = heapq.heappop(pq)
        cost = -cost

        if blocks:
            # Find the color of the top block
            color = blocks[-1]

            # Find the stack with the same color and minimum cost
            dest = None
            for i in range(len(pq)):
                _, index, stack = pq[i]
                if stack and stack[-1] == color and (dest is None or costs[index] < costs[dest]):
                    dest = index

            if dest is None:
                # Create a new stack with the color of the top block
                heapq.heappush(pq, (costs[len(pq)], len(pq), [color]))
                dest = len(pq) - 1
            else:
                # Move the top block to the found stack
                heapq.heappush(pq, (costs[dest], dest, stack + [color]))

            # Add the transfer pair to the list
            transfer_pairs.append((src, dest))

    return transfer_pairs

stacks = [['Yellow', 'Blue', 'Blue', 'Green'], [], ['Yellow', 'Green', 'Red', 'Red'], ['Green', 'Red', 'Yellow', 'Blue'], [], []]
costs = [7, 3, 5, 5, 1, 3]

# Convert the stacks to the colors
stacks = [[color for _ in range(len(stack))] for color in stacks]

print(restricted_sorting(stacks, costs))
