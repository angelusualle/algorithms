class Knapsack():
    def __init__(self, max_weight, values, weights):
        if len(values) != len(weights):
            raise Exception("Length of values list and weights list not the same.")
        self.values = values
        self.weights = weights
        self.max_weight = max_weight

        # init configuration, stuff as much as possible as a way to bound further exporation
        init_config = ''
        init_config_score = 0
        init_weight = 0
        for i, val in enumerate(values):
            wt = init_weight + weights[i]
            if wt < self.max_weight:
                init_config += str(val) + ' '
                init_config_score += val
                init_weight += weights[i]
        self.best_score = init_config_score
        self.best_config_weight = init_weight
        self.best_config= init_config        

    def solve(self, values=None, weights=None, config='', current_weight=0, current_score=0):
        if values is None:
            values = self.values
        if weights is None:
            weights = self.weights
        if current_score > self.best_score:
            self.best_score = current_score
            self.best_config_weight = current_weight
            self.best_config = config
        if len(values) == 0:
            return
        # Branch and bound trick
        if sum(values) + current_score < self.best_score:
            return
        next_val= values[0]
        next_weight = weights[0]
        if next_weight + current_weight < self.max_weight:
            self.solve(values[1:], weights[1:], config + str(next_val) + ' ', current_weight+next_weight, current_score+next_val)
        self.solve(values[1:], weights[1:], config, current_weight, current_score)
