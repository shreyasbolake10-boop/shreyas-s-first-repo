# SLE-3 C4 Diagrams — 8-Puzzle Solver

The SLE-3 submission uses four C4 levels for the 8-Puzzle Solver from SLE-2.

## Level 1 — Context

Student/User -> 8-Puzzle Solver -> Solution Result

## Level 2 — Containers

Input Module -> Search Engine -> Heuristic Module / Visited-Memory -> Output Module

## Level 3 — Components inside Search Engine

Frontier / Open List -> State Expansion -> Goal Test -> Result Generation

## Level 4 — Code Overview

- State / SearchResult
- neighbors(state)
- bfs(start, goal)
- a_star(start, goal)
- manhattan(state)
- benchmark(func)
- main()
