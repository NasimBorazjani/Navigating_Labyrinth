
def sort_it(tubes):
    moves = []
    colors = set()
    
    for tube in tubes:
        colors.update(tube)
    
    sorted_tubes = [sorted(tube, key=lambda x: list(colors).index(x)) for tube in tubes]
    
    for color in colors:
        for i in range(len(tubes)):
            if color in tubes[i]:
                j = sorted_tubes[i].index(color)
                while j > 0:
                    k = i
                    while len(sorted_tubes[k]) == 8 or (len(tubes[k]) > 0 and tubes[k][-1] == color):
                        k = (k + 1) % 3
                    moves.append((i, k))
                    tubes[k].append(tubes[i].pop())
                    sorted_tubes[k].insert(0, color)
                    j -= 1
    
    return moves

initial_tubes = [['Red', 'Green', 'Green', 'Red', 'Blue'], ['Red', 'Blue', 'Green', 'Red', 'Green'], ['Green', 'Blue', 'Blue', 'Blue', 'Red']]
solution = sort_it(initial_tubes)

print(solution)
