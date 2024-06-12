
import heapq

def restricted_sorting(stacks, costs):
    # Initialize the stacks and costs
    stacks = [list(reversed(stack)) for stack in stacks]
    empty_stacks = [i for i, stack in enumerate(stacks) if not stack]
    heap = [(costs[i], i, None) for i in empty_stacks]

    # Initialize the result
    result = []

    while heap:
        cost, src, _ = heapq.heappop(heap)
        if not stacks[src]:
            continue
        shade = stacks[src].pop()
        if not stacks[src]:
            empty_stacks.remove(src)
        for dst in empty_stacks:
            if not stacks[dst] or stacks[dst][-1] == shade:
                heapq.heappush(heap, (costs[dst], dst, shade))
                result.append((src, dst))
                break
        else:
            stacks[src].append(shade)

    return result

stacks = [['Green', 'Red', 'Blue', 'Blue'], [], ['Yellow', 'Red', 'Green', 'Green'], [], [], ['Red', 'Yellow', 'Blue', 'Yellow']]
costs = [4, 2, 2, 7, 4, 5]
shades = list(map(lambda x: x[0], stacks))
stacks = [list(filter(lambda x: x[1] == shade, enumerate(shades))) for shade in set(shades)]

print(restricted_sorting(stacks, costs))
