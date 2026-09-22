# SLE-2 Profiling Report — BFS vs A* (8-Puzzle)

Course: **02AML204 – Introduction to Artificial Intelligence**

This repository contains the empirical performance-analysis experiment for SLE-2.

## Experiment

Two search algorithms solve the **same 8-puzzle**:

- **Algorithm A:** Breadth-First Search (BFS)
- **Algorithm B:** A* Search with Manhattan-distance heuristic

The program measures average execution time with Python's `timeit` and nodes expanded by each algorithm.

## Run

Requires Python 3.9+.

```bash
python profiling.py
```

The script runs each algorithm 5 times and prints the average time, nodes expanded, solution depth, and raw timing samples.

**Important:** Run the experiment yourself and use the numbers printed on your machine in the final report. Do not submit placeholder or copied measurements.

## Fair comparison

Both algorithms use the same start state, goal state, Python environment, and measurement method.

## Files

- `profiling.py` — BFS, A*, Manhattan heuristic, node counter, and benchmark.
- `report_template.md` — SLE-2 report structure.
- `requirements.txt` — no third-party packages required.
