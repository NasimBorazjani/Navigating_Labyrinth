
import heapq

def restricted_sorting(stacks, costs):
    moves = []
    visited = set()
    heap = [(0, stacks, [])]
    while heap:
        cost, stacks, path = heapq.heappop(heap)
        state = tuple(tuple(stack) for stack in stacks)
        if state in visited:
            continue
        visited.add(state)
        if is_sorted(stacks):
            moves = path
            break
        for i in range(8):
            if not stacks[i]:
                continue
            for j in range(8):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 5:
                    new_stacks = [list(stack) for stack in stacks]
                    block = new_stacks[i].pop()
                    new_stacks[j].append(block)
                    new_path = path + [(i, j)]
                    new_cost = cost + costs[j]
                    heapq.heappush(heap, (new_cost, new_stacks, new_path))
    return moves

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [['Green', 'Green', 'Red', 'Blue', 'Red'], ['Black', 'Red', 'Black', 'Red', 'Green'], ['Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Blue', 'Yellow', 'Blue', 'Yellow', 'Yellow'], [], [], []]
costs = {0: 5, 1: 2, 2: 8, 3: 7, 4: 5, 5: 6, 6: 1, 7: 1}
print(restricted_sorting(stacks, costs))
