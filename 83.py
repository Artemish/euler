from collections import defaultdict
from heapq import heappush

INFINITY = 2**31

def dijkstra(g, s):
    Q = []
    dist = {}
    prev = {}

    for v in g:
        heappush(h, (INFINITY, v))

    dist[s] = 0

    while len(Q) > 0:
        g
