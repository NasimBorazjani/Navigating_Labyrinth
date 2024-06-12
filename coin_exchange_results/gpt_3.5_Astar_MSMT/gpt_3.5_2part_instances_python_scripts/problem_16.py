
import heapq

def initialize():
    coins = [11, 13, 22, 11, 16, 20, 10, 10, 17, 21, 6, 6, 15, 15, 21, 6, 4, 16, 9, 11, 3, 13, 2, 9, 11, 1, 7, 2, 2, 12, 5, 2, 11, 16, 20, 9, 2, 4, 10, 17, 11, 22, 11, 2, 18, 23, 15, 22, 11, 15, 20, 9]
    tax_values = {6: 2, 11: 9, 3: 3, 15: 2, 9: 1, 18: 13, 22: 13, 16: 5, 21: 2, 5: 2, 12: 4, 7: 5, 4: 3, 13: 2, 1: 1, 20: 14, 2: 1, 10: 4, 23: 15, 17: 9}
    target_sum = 223
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
