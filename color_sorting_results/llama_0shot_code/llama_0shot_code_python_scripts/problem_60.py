
from collections import deque

def move_ball(tubes, from_tube, to_tube):
    """
    Moves a ball from one tube to another.
    """
    # Remove a ball from the 'from_tube'
    ball = tubes[from_tube].pop()
    
    # Add the ball to the 'to_tube'
    tubes[to_tube].append(ball)

def generate_next_states(tubes):
    """
    Generates all the possible next states from the current state.
    """
    next_states = []
    
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and len(tubes[i]) > 0 and (len(tubes[j]) < 8):
                # Create a new list of tubes for the next state
                new_tubes = [tube.copy() for tube in tubes]
                
                # Move the ball from 'i' to 'j'
                move_ball(new_tubes, i, j)
                
                # Add the new state to the list of next states
                next_states.append(new_tubes)
    return next_states

def bfs(initial_tubes, final_tubes):
    """
    Finds the shortest path from the initial state to the final state.
    """
    queue = deque([([], initial_tubes)])
    
    while queue:
        path, tubes = queue.popleft()
        
        if tubes == final_tubes:
            return path
        
        next_states = generate_next_states(tubes)
        
        for next_state in next_states:
            move = (tubes.index(next_state), next_state.index(next_state[0]))
            new_path = path + [move]
            queue.append((new_path, next_state))

    return None

# The initial state of the tubes
initial_tubes = [['Green', 'Red', 'Blue', 'Blue', 'Green'], 
                 ['Red', 'Green', 'Blue', 'Red', 'Green'], 
                 ['Blue', 'Red', 'Blue', 'Green', 'Red']]

# The final state of the tubes
final_tubes = [['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'], 
               ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'], 
               ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red']]

# Find the shortest path
path = bfs(initial_tubes, final_tubes)

print(path)
