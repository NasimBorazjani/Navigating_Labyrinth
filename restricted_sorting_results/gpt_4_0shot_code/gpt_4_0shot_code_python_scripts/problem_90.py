
import heapq

def solve(stacks, costs):
    moves = []
    heap = [(0, stacks, moves)]
    visited = set()

    while heap:
        cost, stacks, moves = heapq.heappop(heap)
        state = tuple(tuple(stack) for stack in stacks)

        if state in visited:
            continue
        visited.add(state)

        if is_sorted(stacks):
            return moves

        for i in range(len(stacks)):
            if not stacks[i]:
                continue
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 7:
                    new_stacks = [list(stack) for stack in stacks]
                    new_stacks[j].append(new_stacks[i].pop())
                    new_moves = moves + [(i, j)]
                    new_cost = cost + costs[j]
                    heapq.heappush(heap, (new_cost, new_stacks, new_moves))

def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

stacks = [['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'], [], [], ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'], [], ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'], ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'], ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'], [], ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'], [], []]
costs = {0: 2, 1: 7, 2: 2, 3: 2, 4: 4, 5: 13, 6: 4, 7: 6, 8: 8, 9: 6, 10: 10, 11: 10}

print(solve(stacks, costs))
