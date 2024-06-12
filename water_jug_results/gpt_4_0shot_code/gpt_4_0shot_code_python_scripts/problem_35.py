
from collections import deque

jugs = [120, 95, 49, 150, 83, 97, 44, 43]
buckets = [225, 334, 381]
initial_state = (0, 0, 0)
goal_state = tuple(buckets)
actions = [(f'{sign}{jug}', jug) for jug in jugs for sign in '+-']
state_action_dict = {initial_state: []}

queue = deque([initial_state])
while queue:
    current_state = queue.popleft()
    for action, jug in actions:
        next_state = list(current_state)
        if action[0] == '+':
            for i in range(len(buckets)):
                if next_state[i] + jug <= buckets[i] and (i == 0 or next_state[i] + jug <= next_state[i - 1]):
                    next_state[i] += jug
                    break
        else:
            for i in reversed(range(len(buckets))):
                if next_state[i] - jug >= 0 and (i == len(buckets) - 1 or next_state[i] - jug >= next_state[i + 1]):
                    next_state[i] -= jug
                    break
        next_state = tuple(next_state)
        if next_state not in state_action_dict:
            state_action_dict[next_state] = state_action_dict[current_state] + [action]
            if next_state == goal_state:
                print(state_action_dict[next_state])
                queue = None
                break
            queue.append(next_state)
