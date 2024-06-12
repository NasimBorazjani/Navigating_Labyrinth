
import heapq

def restricted_sorting(stacks):
    colors = {}
    for i, stack in enumerate(stacks):
        for color in stack:
            if color not in colors:
                colors[color] = []
            colors[color].append(i)

    for color in colors:
        stack_ids = colors[color]
        heap = []
        for stack_id in stack_ids:
            stack = stacks[stack_id]
            cost = len(stack)
            if cost < 5:
                heapq.heappush(heap, (cost, stack_id))

        while len(heap) > 1:
            cost1, stack_id1 = heapq.heappop(heap)
            cost2, stack_id2 = heapq.heappop(heap)
            if stack_id1 != stack_id2:
                stacks[stack_id1].append(stacks[stack_id2].pop())
                if len(stacks[stack_id2]) < 5:
                    heapq.heappush(heap, (len(stacks[stack_id2]), stack_id2))

    transfer_pairs = []
    for i in range(8):
        for j in range(i+1, 8):
            if stacks[i] and stacks[j]:
                if stacks[i][-1] == stacks[j][-1]:
                    stacks[j].append(stacks[i].pop())
                    transfer_pairs.append((i, j))

    return transfer_pairs

stacks = [[], [], [], ['Blue', 'Yellow', 'Red', 'Blue', 'Black'], 
          ['Red', 'Yellow', 'Blue', 'Yellow', 'Blue'], 
          ['Green', 'Red', 'Black', 'Red', 'Yellow'], [], 
          ['Green', 'Green', 'Black', 'Green', 'Black']]

print(restricted_sorting(stacks))
