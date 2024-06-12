
import heapq

def restricted_sorting(stacks, costs):
    # Initialize priority queue with costs
    queue = [(cost, i) for i, cost in enumerate(costs)]
    heapq.heapify(queue)

    # Initialize dictionaries to keep track of the top block and the number of blocks of each shade in each stack
    top_block = {}
    shades_count = {}
    for i, blocks in enumerate(stacks):
        if blocks:
            top_block[i] = blocks[-1]
            shades_count[i] = {block: blocks.count(block) for block in set(blocks)}
        else:
            top_block[i] = None
            shades_count[i] = {}

    # Initialize lists to keep track of the transfer pairs and their costs
    transfer_pairs = []
    total_cost = 0

    # Move blocks until all stacks are sorted
    while True:
        moved = False
        for i, blocks in enumerate(stacks):
            if not blocks:
                continue
            shade = blocks[-1]
            if len(blocks) == 1:
                stacks[i] = []
                moved = True
                break
            else:
                # Find stack to move block to
                for j in range(10):
                    if j != i and (not top_block[j] or top_block[j] == shade):
                        cost = heapq.heappop(queue)[0]
                        heapq.heappush(queue, (cost, j))
                        stacks[j].append(shades_count[i][shade])
                        stacks[i].remove(shades_count[i][shade])
                        shades_count[i][shade] -= 1
                        if not shades_count[i][shade]:
                            del shades_count[i][shade]
                        top_block[i] = stacks[i][-1] if stacks[i] else None
                        top_block[j] = shade
                        total_cost += cost
                        transfer_pairs.append((i, j, cost))
                        moved = True
                        break
                if moved:
                    break

        # If no blocks were moved in the last iteration, all stacks are sorted
        if not moved:
            break

    # Return transfer pairs with their costs
    return transfer_pairs

stacks = [[], [], ['Blue', 'Yellow', 'Red', 'Black', 'White', 'Blue'], ['Blue', 'Green', 'Yellow', 'Red', 'Red', 'White'], [], ['Red', 'Black', 'White', 'Yellow', 'White', 'Green'], [], ['Black', 'Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Red', 'Green', 'Green', 'Blue', 'Yellow', 'White']]
costs = [6, 10, 8, 3, 5, 7, 10, 6, 3, 8]
print(restricted_sorting(stacks, costs))
