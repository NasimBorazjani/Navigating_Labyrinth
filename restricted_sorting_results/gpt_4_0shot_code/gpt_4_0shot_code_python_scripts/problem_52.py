
import heapq

def restricted_sorting(stacks):
    costs = {0: 6, 1: 4, 2: 3, 3: 8, 4: 7, 5: 5, 6: 9, 7: 9}
    goal = [['Blue']*4, ['Red']*4, ['Yellow']*4, ['Green']*4, ['Black']*4, [], [], []]
    queue = [(0, stacks, [])]
    visited = set()

    while queue:
        cost, state, actions = heapq.heappop(queue)
        if state == goal:
            return actions
        if str(state) in visited:
            continue
        visited.add(str(state))
        for i in range(8):
            if state[i]:
                for j in range(8):
                    if i != j and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < 5:
                        new_state = [list(s) for s in state]
                        new_state[j].append(new_state[i].pop())
                        new_cost = cost + costs[j]
                        new_actions = actions + [(i, j)]
                        heapq.heappush(queue, (new_cost, new_state, new_actions))

stacks = [[], [], [], ['Blue', 'Yellow', 'Red', 'Blue', 'Black'], ['Red', 'Yellow', 'Blue', 'Yellow', 'Blue'], ['Green', 'Red', 'Black', 'Red', 'Yellow'], [], ['Green', 'Green', 'Black', 'Green', 'Black']]
print(restricted_sorting(stacks))
