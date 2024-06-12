
import heapq

def restricted_sorting(stacks, costs):
    moves = []
    heap = [(0, stacks, [])]
    visited = set()

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
                    new_stacks[j].append(new_stacks[i].pop())
                    new_cost = cost + costs[j]
                    new_path = path + [(i, j)]
                    heapq.heappush(heap, (new_cost, new_stacks, new_path))

    return moves

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [[], ['Blue', 'Black', 'Blue', 'Yellow', 'Red'], ['Red', 'Green', 'Black', 'Green', 'Black'], [], ['Red', 'Red', 'Green', 'Yellow', 'Yellow'], [], [], ['Blue', 'Yellow', 'Green', 'Black', 'Blue']]
costs = {0: 3, 1: 2, 2: 1, 3: 7, 4: 5, 5: 5, 6: 6, 7: 4}

print(restricted_sorting(stacks, costs))
