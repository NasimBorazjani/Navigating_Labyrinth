
def move_ball(from_tube, to_tube, tubes):
    # Remove a ball from the 'from_tube' and add it to the 'to_tube'
    ball = tubes[from_tube].pop()
    tubes[to_tube].append(ball)
    # Return the move as a tuple
    return (from_tube, to_tube)

def sort_balls(tubes):
    # List to store the moves made
    moves = []
    # Continue until there are no more balls to move
    while True:
        # Flags to check if there are balls to move
        ball_to_move = False
        # Iterate over the tubes
        for i in range(len(tubes)):
            # If the tube is not empty
            if tubes[i]:
                # Check if the current tube has a ball of different color in it
                for j in range(len(tubes)):
                    if i != j and tubes[i][-1] != tubes[j][-1] and len(tubes[j]) < 8:
                        # If so, move the ball to the other tube
                        move = move_ball(i, j, tubes)
                        moves.append(move)
                        ball_to_move = True
                        break
                if ball_to_move:
                    break
        # If no balls were moved in the inner loop, all balls are sorted
        if not ball_to_move:
            break
    return moves

# Initial state of the tubes
tubes = [['Blue', 'Red', 'Red', 'Blue', 'Red'], 
         ['Green', 'Blue', 'Blue', 'Red', 'Green'], 
         ['Blue', 'Green', 'Red', 'Green', 'Green']]

print(sort_balls(tubes))
