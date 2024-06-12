
def sort_it(tubes, color, source, target, auxiliary):
    moves = []
    if color in tubes[source]:
        # Move balls of other colors from source to auxiliary
        while tubes[source][-1] != color:
            move_ball(tubes, source, auxiliary)
            moves.append((source, auxiliary))
        # Move the ball of the current color from source to target
        move_ball(tubes, source, target)
        moves.append((source, target))
        # Move the balls of other colors from auxiliary back to source
        while tubes[auxiliary] and tubes[auxiliary][-1] != color:
            move_ball(tubes, auxiliary, source)
            moves.append((auxiliary, source))
        # Repeat the process for the remaining balls of the current color
        moves.extend(sort_it(tubes, color, source, target, auxiliary))
    return moves

def move_ball(tubes, source, target):
    tubes[target].append(tubes[source].pop())

tubes = [['Red', 'Blue', 'Blue', 'Red'], ['Blue', 'Green', 'Blue', 'Green'], ['Green', 'Red', 'Green', 'Red']]
colors = ['Red', 'Blue', 'Green']
moves = []
for color in colors:
    for i in range(3):
        if color in tubes[i]:
            moves.extend(sort_it(tubes, color, i, (i+1)%3, (i+2)%3))
print(moves)
