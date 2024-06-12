
from collections import deque

def bfs(initial_state, goal_state, cost):
    queue = deque([initial_state])
    parent = {initial_state: None}
    cost_so_far = {initial_state: 0}

    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            break

        for next_state in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + cost[next_state]

            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                parent[next_state] = current_state
                queue.append(next_state)

    return parent, cost_so_far

def get_neighbors(state):
    # This function returns all the neighboring states of the given state.
    # A neighboring state is a state that can be reached by transferring one block.

def get_path(parent, initial_state, goal_state):
    path = []
    current_state = goal_state

    while current_state != initial_state:
        previous_state = parent[current_state]
        path.append((previous_state, current_state))
        current_state = previous_state

    path.reverse()
    return path
