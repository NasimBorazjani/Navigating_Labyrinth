
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
        for i in range(6):
            if not stacks[i]:
                continue
            for j in range(6):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 4:
                    new_stacks = [list(stack) for stack in stacks]
                    block = new_stacks[i].pop()
                    new_stacks[j].append(block)
                    new_cost = cost + costs[j]
                    new_path = path + [(i, j)]
                    heapq.heappush(heap, (new_cost, new_stacks, new_path))
    return moves

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [['Green', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Yellow', 'Blue'], [], ['Green', 'Yellow', 'Red', 'Yellow'], [], []]
costs = {0: 2, 1: 7, 2: 4, 3: 7, 4: 6, 5: 3}
print(restricted_sorting(stacks, costs))
