
import heapq

def initialize():
    coins = [8, 8, 6, 36, 7, 36, 33, 3, 31, 17, 21, 28, 41, 17, 23, 16, 39, 2, 3, 40, 23, 20, 5, 30, 8, 28, 17, 34, 38, 26, 16, 21, 15, 21, 11, 33, 5, 33, 2, 27, 26, 21, 14, 13, 7, 23]
    tax_values = {28: 16, 5: 1, 3: 3, 40: 18, 33: 20, 34: 12, 20: 4, 39: 13, 2: 2, 31: 11, 36: 2, 17: 14, 7: 1, 14: 6, 23: 12, 8: 1, 30: 15, 27: 13, 15: 2, 21: 3, 11: 6, 26: 14, 41: 2, 38: 10, 6: 5, 16: 4, 13: 11}
    target_sum = 403
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
