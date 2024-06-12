
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def is_sorted(tubes):
        for tube in tubes:
            if len(set(tube)) != 1:
                return False
        return True
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)
    
    while not is_sorted(tubes):
        for color in colors:
            for i in range(3):
                if tubes[i][0] == color:
                    for j in range(3):
                        if i != j and len(tubes[j]) < 9 and tubes[j][0] != color:
                            move_ball(i, j)
    
    return moves

tubes = [['Red', 'Green', 'Blue', 'Red', 'Red', 'Blue'], 
         ['Green', 'Red', 'Green', 'Green', 'Blue', 'Red'], 
         ['Green', 'Blue', 'Green', 'Blue', 'Blue', 'Red']]

solution = sort_it(tubes)
print(solution)
