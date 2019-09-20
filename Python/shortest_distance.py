"""
Your task: Define a function which takes 3 arguments: the length a , width b, and height c of the bug's "world",
and finds the shortest distance needed to walk from start to finish. The dimensions will be positive numbers.

Note: The bug cannot fly and has to maintain contact with a surface at all times but can walk up walls.
Example: shortestDistance(1,2,3) === 4.242640687119285.
Hint 1: Consider how many different routes can be made to get from start to finish. If stuck for where to start,
click here for general guidance.
Hint 2: Consider using paper and opening up the net of a cuboid (and think if there are multiple ways this can be
viewed) and play around with it to find the shortest length.
"""
import numpy as np
import sympy as sy

def shortest_distance(a, b, c):
    x, d = sy.symbols("x d")
    d = sy.sqrt((x-a)**2 + (x-b)**2 + (x-c)**2)
    print(d)
    df = sy.diff(d, x)
    print(df)
    solucion = sy.solve(sy.Eq(df,0), x)
    print(d.subs(x, solucion[0]))
    
print(shortest_distance(1,2,3))