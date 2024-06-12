
import heapq

def initialize():
    coins = [30, 28, 81, 26, 24, 20, 5, 18, 33, 19, 30, 27, 6, 10, 22, 10, 33, 10, 15, 26, 9, 6, 22, 31, 36, 16, 4, 11, 24, 7, 17, 30, 3, 7, 8, 8, 34]
    tax_values = {24: 7, 22: 3, 11: 10, 28: 17, 7: 7, 20: 10, 5: 2, 8: 2, 9: 5, 15: 14, 81: 17, 30: 5, 31: 17, 33: 9, 18: 3, 36: 2, 16: 14, 10: 1, 19: 15, 3: 1, 34: 12, 26: 13, 6: 3, 4: 1, 27: 11, 17: 5}
    target_sum = 387
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
