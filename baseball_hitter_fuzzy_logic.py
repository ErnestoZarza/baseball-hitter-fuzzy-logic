__author__ = 'Ernesto Zarza'
# import numpy as np

batting = {"Bad Hitter": (1, 250), "Average Hitter": (245, 280), "Good Hitter": (270, 500)}
types = ["Bad Hitter", "Average Hitter", "Good Hitter"]


def membership_function(x, point_a, point_b):
    if x < point_a or x > point_b:
        return 0
    else:
        return float(x - point_a) / float(point_b - point_a)


def type_hitter(x):
    hitter = types[0]
    higher = 0.0

    for hitter_type in types:
        temp = membership_function(x, batting[hitter_type][0], batting[hitter_type][1])
        if higher < temp:
            higher = temp
            hitter = hitter_type

    return hitter, higher


def or_fuzzy(x, y):
    return max(x, y)


def and_fuzzy(x, y):
    return min(x, y)


def defuzzyfication(x):
    higher = -1
    for i in range(3):
        temp = membership_function(x, batting[types[i]][0], batting[types[i]][1])
        if higher < temp:
            higher = temp
    return higher


def play_fuzzy_rules(average, objetiv):
    hitter = type_hitter(average)[0]
    if (hitter == "Bad Hitter" or hitter == "Average Hitter") and objetiv == "Produce":
        action = "Touch the Ball"
    elif hitter == "Average Hitter" and objetiv == "Get to the base":
        action = "Touch the Ball"
    else:
        action = "Hit hard"

    return action


print(defuzzyfication(260))

print(play_fuzzy_rules(260, "Get to the base"))
