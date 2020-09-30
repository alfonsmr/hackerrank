# https://www.hackerrank.com/challenges/30-operators/problem

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)

    cost = meal_cost + tip + tax

    print(round(cost)) 