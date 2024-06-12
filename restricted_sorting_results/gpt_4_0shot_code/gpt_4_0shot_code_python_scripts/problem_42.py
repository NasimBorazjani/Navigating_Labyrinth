
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

        for i in range(len(stacks)):
            if not stacks[i]:
                continue

            for j in range(len(stacks)):
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

stacks = [['Blue', 'Black', 'Yellow', 'Black', 'Red'], ['Blue', 'Blue', 'Green', 'Black', 'Yellow'], [], ['Yellow', 'Red', 'Red', 'Green', 'Green'], [], [], ['Red', 'Blue', 'Black', 'Green', 'Yellow'], []]
costs = {0: 7, 1: 5, 2: 7, 3: 2, 4: 6, 5: 7, 6: 5, 7: 3}

print(restricted_sorting(stacks, costs))
