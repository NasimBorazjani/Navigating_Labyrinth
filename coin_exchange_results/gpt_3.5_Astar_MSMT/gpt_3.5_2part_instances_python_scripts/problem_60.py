
import heapq

def initialize():
    coins = [28, 2, 4, 7, 11, 26, 14, 8, 23, 29, 18, 13, 26, 21, 10, 26, 8, 33, 9, 15, 4, 21, 19, 3, 7, 10, 4, 7, 16, 16, 11, 33, 12, 23, 5, 3, 26, 7, 17, 30, 22, 22, 6, 16, 18, 25, 26, 11, 13, 23, 17, 11, 20, 12]
    tax_values = {10: 6, 18: 17, 33: 15, 16: 16, 3: 2, 30: 18, 13: 3, 21: 17, 23: 4, 12: 1, 7: 6, 17: 7, 4: 2, 6: 5, 2: 2, 11: 5, 14: 14, 29: 1, 20: 7, 8: 3, 15: 7, 28: 3, 26: 8, 19: 11, 9: 9, 22: 4, 5: 5, 25: 5}
    target_sum = 339
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
