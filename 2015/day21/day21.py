weapons = [
    {"name":"Dagger",       "cost":8,   "dmg":4 },
    {"name":"Shortsword",   "cost":10,  "dmg":5 },
    {"name":"Warhammer",    "cost":25,  "dmg":6 },
    {"name":"Longsword",    "cost":40,  "dmg":7 },
    {"name":"Greataxe",     "cost":74,  "dmg":8 }
]

armour = [
    {"name":"None",         "cost":0,    "def":0 },
    {"name":"Leather",      "cost":13,   "def":1 },
    {"name":"Chainmail",    "cost":31,   "def":2 },
    {"name":"Splintmail",   "cost":53,   "def":3 },
    {"name":"Bandedmail",   "cost":75,   "def":4 },
    {"name":"Platemail",    "cost":102,  "def":5 },
]

rings = [
    {"name":"None",         "cost":0,   "def":0, "dmg":0 },
    {"name":"None",         "cost":0,   "def":0, "dmg":0 },
    {"name":"DMG+1",        "cost":25,  "def":0, "dmg":1 },
    {"name":"DMG+2",        "cost":50,  "def":0, "dmg":2 },
    {"name":"DMG+3",        "cost":100, "def":0, "dmg":3 },
    {"name":"DEF+1",        "cost":20,  "def":1, "dmg":0 },
    {"name":"DEF+2",        "cost":40,  "def":2, "dmg":0 },
    {"name":"DEF+3",        "cost":80,  "def":3, "dmg":0 },
]

ring_combos = []
for i in range(0, len(rings)):
    for j in range(i + 1, len(rings)):
        ring_combos.append([rings[i], rings[j]])

def max(a, b): return a if a > b else b

import math

min_cost = 9999
max_cost = 0
boss = {"hp": 103.0, "dmg": 9, "def": 2}
player = {"hp": 100.0}
for wpn in weapons:
    for arm in armour:
        for rngs in ring_combos:
            r1 = rngs[0]
            r2 = rngs[1]
            player["dmg"] = wpn["dmg"] + r1["dmg"] + r2["dmg"]
            player["def"] = arm["def"] + r1["def"] + r2["def"]
            cost = wpn["cost"] + arm["cost"] + r1["cost"] + r2["cost"]
            pd = max(player["dmg"] - boss["def"], 1)
            bd = max(boss["dmg"] - player["def"], 1)
            pm = math.ceil(boss["hp"] / pd)
            bm = math.ceil(player["hp"] / bd)
            if pm <= bm:
                if cost < min_cost: min_cost = cost
            else:
                if cost > max_cost:
                    max_cost = cost

print("Minimum cost to win the fight", min_cost)
print("Maximum cost to lose the fight", max_cost)