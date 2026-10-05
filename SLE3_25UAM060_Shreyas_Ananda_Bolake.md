# SLE-3: Architectural Design (Full C4 Model)

**Course:** 02AML204 - Introduction to Artificial Intelligence  
**PRN:** 25UAM060  
**Name:** Shreyas Ananda Bolake  
**Division:** A  
**Date:** 05/10/2026  
**GitHub / Portfolio:** https://github.com/shreyasbolake10-boop/shreyas-s-first-repo

## 1. System Title & Short Description

### 8-Puzzle Solver using BFS and A*

The 8-Puzzle Solver is an AI search system that finds a sequence of moves from a starting 3x3 tile arrangement to the goal state. It models each puzzle configuration as a search state and generates valid neighboring states by moving the blank tile. The system implements Breadth-First Search (BFS) and A* Search, with A* guided by the Manhattan-distance heuristic. The same architecture supports both algorithms, making comparison and future extension straightforward.

## 2. Context Diagram (Level 1)

**Student/User -> 8-Puzzle Solver -> Solution Result**

- **Student/User:** Provides the start state and selects BFS or A*.
- **8-Puzzle Solver:** Searches the state space for the goal state.
- **Solution Result:** Returns path/depth/search information.

## 3. Container Diagram (Level 2)

1. **Input Module** - Accepts the puzzle state and algorithm choice.
2. **Search Engine** - Runs BFS or A* search.
3. **Heuristic Module** - Calculates Manhattan distance for A*.
4. **Visited / Memory** - Stores visited states or best-known costs.
5. **Output Module** - Reports the final search result.

**Flow:** Input Module -> Search Engine -> Heuristic Module / Visited-Memory -> Output Module

## 4. Component Diagram (Level 3)

### Components inside Search Engine

1. **Frontier / Open List** - Queue for BFS and priority queue for A*.
2. **State Expansion** - Generates valid neighbouring puzzle states.
3. **Goal Test** - Checks whether the current state equals the goal state.
4. **Path / Result Generation** - Records the search outcome and result information.

## 5. Code Level Overview (Level 4)

- `State / SearchResult` - Represents a puzzle state and stores search results.
- `neighbors(state)` - Generates valid next states by moving the blank tile.
- `bfs(start, goal)` - Performs Breadth-First Search.
- `a_star(start, goal)` - Performs A* Search.
- `manhattan(state)` - Calculates the Manhattan-distance heuristic.
- `benchmark(func)` - Measures algorithm runtime for profiling.
- `main()` - Runs the comparison and displays results.

## 6. Design Decisions

The architecture separates input, search, heuristic calculation, memory and output so BFS and A* can share the same state representation. Manhattan distance is isolated so the heuristic can be changed without redesigning the search engine. The modular structure also makes it easier to add other AI search algorithms later.

## 7. AI Contribution Note

- **AI tools used:** ChatGPT
- **What AI helped with:** Understanding the C4 structure, organizing the architecture, and improving report wording and diagram layout.
- **What I did myself:** I used and understood the BFS/A* implementation, ran the profiling experiment, checked the results, and prepared the final submission.

## 8. Conclusion

This SLE showed how an AI search program can be described at four architectural levels: context, container, component and code. The C4 model made the responsibilities of the 8-Puzzle Solver clearer and showed how BFS and A* fit into the same architecture. It also provides a structured foundation for extending the solver with additional search strategies.
