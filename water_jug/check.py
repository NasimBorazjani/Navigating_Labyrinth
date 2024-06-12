def is_feasible(capacities, targets, action_tuples, called_from_correct=False):
    for action in action_tuples:
        if not (action[0] in ['-', '+'] and action[1] in capacities and 1 <= action[2] <= len(targets)):
            if called_from_correct:
                return False, None
            return False
    
    total = [0 for i in range(len(targets))]
    for action in action_tuples:
        bucket_ind = action[2] -1 
        if action[0] == '+':
            total[bucket_ind] += action[1]
            if total[bucket_ind] > targets[bucket_ind]:
                if called_from_correct:
                    return False, None
                return False
        else:
            total[bucket_ind] -= action[1]
            if total[bucket_ind] < 0:
                if called_from_correct:
                    return False, None
                return False
            
        if not all(total[i] <= total[i + 1] for i in range(len(total) - 1)):
            if called_from_correct:
                return False, None
            return False
    
    if called_from_correct:           
        return True, total
    return True
        
def is_correct(capacities, targets, action_tuples):
    feasible, total = is_feasible(capacities, targets, action_tuples, called_from_correct=True)
    if not feasible or total != targets:
        return False, None
    return True, len(action_tuples)
   
"""
action_tuples = [('+', 26, 3), ('+', 40, 3), ('+', 136, 3), ('-', 41, 3), ('+', 136, 3), ('+', 40, 2), ('+', 40, 2), ('+', 44, 2), ('+', 75, 2), ('+', 75, 2), ('+', 40, 1), ('+', 40, 1), ('+', 75, 1), ('+', 75, 1)]
target = [230, 274, 297]
capacities = [44, 41, 136, 26, 75, 40]
print(is_correct(capacities, target, action_tuples))"""

        