from __future__ import annotations

import heapq
import timeit
from collections import deque
from dataclasses import dataclass
from itertools import count
from math import inf

State = tuple[int, ...]
GOAL: State = (1, 2, 3, 4, 5, 6, 7, 8, 0)
START: State = (7, 2, 4, 5, 0, 6, 8, 3, 1)

def neighbors(state: State):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap = nr * 3 + nc
            nxt = list(state)
            nxt[zero], nxt[swap] = nxt[swap], nxt[zero]
            yield tuple(nxt)

def manhattan(state: State) -> int:
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = tile - 1
        r1, c1 = divmod(index, 3)
        r2, c2 = divmod(goal_index, 3)
        distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

@dataclass
class SearchResult:
    found: bool
    depth: int
    nodes_expanded: int

def bfs(start: State, goal: State) -> SearchResult:
    queue = deque([(start, 0)])
    visited = {start}
    expanded = 0
    while queue:
        state, depth = queue.popleft()
        expanded += 1
        if state == goal:
            return SearchResult(True, depth, expanded)
        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, depth + 1))
    return SearchResult(False, -1, expanded)

def a_star(start: State, goal: State) -> SearchResult:
    counter = count()
    heap = [(manhattan(start), 0, next(counter), start)]
    best_g = {start: 0}
    expanded = 0
    while heap:
        _, g, _, state = heapq.heappop(heap)
        if g != best_g.get(state, inf):
            continue
        expanded += 1
        if state == goal:
            return SearchResult(True, g, expanded)
        for nxt in neighbors(state):
            new_g = g + 1
            if new_g < best_g.get(nxt, inf):
                best_g[nxt] = new_g
                heapq.heappush(
                    heap, (new_g + manhattan(nxt), new_g, next(counter), nxt)
                )
    return SearchResult(False, -1, expanded)

def benchmark(func, runs=5):
    result = func(START, GOAL)
    times = timeit.repeat(lambda: func(START, GOAL), repeat=runs, number=1)
    return result, times, sum(times) / len(times)

def main():
    runs = 5
    bfs_result, bfs_times, bfs_avg = benchmark(bfs, runs)
    astar_result, astar_times, astar_avg = benchmark(a_star, runs)

    assert bfs_result.found and astar_result.found
    assert bfs_result.depth == astar_result.depth

    print("SLE-2 PROFILING: BFS vs A* on 8-Puzzle")
    print("=" * 42)
    print(f"Start state: {START}")
    print(f"Goal state : {GOAL}\n")

    print(f"BFS  | Avg time: {bfs_avg * 1000:.3f} ms | "
          f"Nodes: {bfs_result.nodes_expanded} | Depth: {bfs_result.depth}")
    print(f"A*   | Avg time: {astar_avg * 1000:.3f} ms | "
          f"Nodes: {astar_result.nodes_expanded} | Depth: {astar_result.depth}")

    print("\nCOMPARISON TABLE")
    print(f"{'Metric':<22}{'BFS':>12}{'A*':>12}")
    print("-" * 46)
    print(f"{'Avg. Time (ms)':<22}{bfs_avg*1000:>12.3f}{astar_avg*1000:>12.3f}")
    print(f"{'Nodes Expanded':<22}{bfs_result.nodes_expanded:>12}{astar_result.nodes_expanded:>12}")
    print(f"{'Solution Depth':<22}{bfs_result.depth:>12}{astar_result.depth:>12}")

    print("\nRaw timing samples (ms):")
    print("BFS:", [round(t * 1000, 3) for t in bfs_times])
    print("A* :", [round(t * 1000, 3) for t in astar_times])

if __name__ == "__main__":
    main()
