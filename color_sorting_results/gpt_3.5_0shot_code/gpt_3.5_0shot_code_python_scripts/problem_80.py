
def sort_it(tubes):
    moves = []
    colors = ['Red', 'Green', 'Blue']
    
    def find_color_index(color):
        for i in range(len(tubes)):
            if tubes[i][0] == color:
                return i
        return -1
    
    def move_ball(from_tube, to_tube):
        moves.append((from_tube, to_tube))
        ball = tubes[from_tube].pop(0)
        tubes[to_tube].insert(0, ball)
    
    for color in colors:
        while True:
            color_index = find_color_index(color)
            if color_index == -1:
                break
            if tubes[color_index].count(color) == 9:
                break
            empty_tube = find_color_index(None)
            if empty_tube == -1:
                empty_tube = tubes.index(min(tubes, key=len))
            move_ball(color_index, empty_tube)
    
    return moves

tubes = [['Blue', 'Red', 'Blue', 'Green', 'Blue', 'Green'], ['Green', 'Green', 'Green', 'Blue', 'Blue', 'Red'], ['Green', 'Blue', 'Red', 'Red', 'Red', 'Red']]
result = sort_it(tubes)
print(result)
