
def move_ball(tubes, from_tube, to_tube):
    # Remove a ball from the 'from_tube' and add it to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)
    return tubes

def sort_balls(tubes):
    # Initialize the list of moves
    moves = []
    
    # Keep simulating the process until all balls are sorted
    while True:
        changed = False
        
        # For each tube
        for i in range(len(tubes)):
            # If the tube is not empty
            if tubes[i]:
                # For each other tube
                for j in range(len(tubes)):
                    # If the other tube is not the same and not full
                    if i != j and len(tubes[j]) != 9:
                        # If the last ball in the 'i' tube has the same color as the last ball in the 'j' tube
                        if tubes[i][-1] == tubes[j][-1]:
                            # Move the ball from the 'i' tube to the 'j' tube
                            tubes = move_ball(tubes, i, j)
                            moves.append((i, j))
                            changed = True
                            break
                
                # If a ball has been moved, break the loop to start a new simulation
                if changed:
                    break
                
        # If no balls have been moved in a simulation, the sorting is finished
        if not changed:
            break
    
    return moves

# Test the function with the given initial state
tubes = [['Green', 'Red', 'Red', 'Red', 'Green', 'Green'], 
         ['Green', 'Red', 'Red', 'Blue', 'Red', 'Blue'], 
         ['Blue', 'Blue', 'Blue', 'Green', 'Blue', 'Green']]

print(sort_balls(tubes))
