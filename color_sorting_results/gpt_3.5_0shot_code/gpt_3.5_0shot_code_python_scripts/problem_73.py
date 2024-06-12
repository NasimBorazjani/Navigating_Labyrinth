
def sort_it(tubes):
    target_tubes = [[], [], []]
    for tube in tubes:
        for ball in tube:
            target_tubes[tube.index(ball)].append(ball)
    
    moves = []
    for i in range(8):
        for j in range(3):
            if tubes[j] and tubes[j][-1] == target_tubes[j][i]:
                continue
            for k in range(3):
                if tubes[k] and tubes[k][-1] == target_tubes[j][i]:
                    moves.append((k, j))
                    tubes[k].pop()
                    tubes[j].append(target_tubes[j][i])
                    break
    
    return moves

initial_tubes = [['Red', 'Green', 'Red', 'Blue', 'Green'], ['Red', 'Blue', 'Green', 'Blue', 'Blue'], ['Green', 'Red', 'Red', 'Green', 'Blue']]
result = sort_it(initial_tubes)
print(result)
