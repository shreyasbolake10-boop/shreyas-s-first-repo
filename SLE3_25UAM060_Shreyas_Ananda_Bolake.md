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

The Context view shows the complete system boundary and the external actor interacting with it.

```text
+-------------------+        +-------------------------+        +-------------------+
|   Student / User  | -----> |    8-Puzzle Solver      | -----> |  Solution Result  |
|                   |        |  Context / System       |        |  Path + Depth     |
+-------------------+        +-------------------------+        +-------------------+
        |                              |
        | Start state + algorithm      | Search / solve
        +------------------------------>
```

**Explanation:** The user provides the start state and chooses BFS or A*. The 8-Puzzle Solver performs the search and returns the solution information to the user.

## 3. Container Diagram (Level 2)

```text
+--------------+      +----------------+      +-------------------+
| Input Module | ---> |  Search Engine | ---> | Output Module     |
+--------------+      +-------+--------+      +-------------------+
                              |
                        +-----+------+
                        |            |
                        v            v
                 +-------------+  +----------------+
                 |  Heuristic  |  | Visited /      |
                 |   Module    |  | Memory         |
                 +-------------+  +----------------+
```

**Container responsibilities:**

- **Input Module:** Accepts the puzzle state and selected algorithm.
- **Search Engine:** Executes BFS or A* and coordinates the search.
- **Heuristic Module:** Calculates Manhattan distance for A*.
- **Visited / Memory:** Stores visited states or best-known costs to reduce repeated work.
- **Output Module:** Presents the final search result and solution depth.

## 4. Component Diagram (Level 3)

**Scope: Search Engine container only.**

```text
+------------------------------------------------------+
|                   SEARCH ENGINE                     |
|                                                      |
|  +------------------+     +----------------------+  |
|  | Frontier / Open  | --> | State Expansion      |  |
|  | List             |     | Generate neighbours  |  |
|  +------------------+     +----------+-----------+  |
|                                       |
|                                       v
|                            +----------------------+  |
|                            | Goal Test            |  |
|                            +----------+-----------+  |
|                                       |
|                                       v
|                            +----------------------+  |
|                            | Path / Result        |  |
|                            | Generation           |  |
|                            +----------------------+  |
+------------------------------------------------------+
```

**Explanation:** The frontier stores states waiting for expansion; BFS uses a queue while A* uses a priority queue. State Expansion generates legal moves. Goal Test checks the target state, and Result Generation produces the final search result.

## 5. Code Level Overview (Level 4)

```text
+------------------------------------------------+
|              CODE LEVEL OVERVIEW              |
+------------------------------------------------+
| State / SearchResult                           |
|   -> puzzle state + search statistics          |
|                                                |
| neighbors(state)                               |
|   -> generates legal neighbouring states       |
|                                                |
| bfs(start, goal)                               |
|   -> Breadth-First Search                     |
|                                                |
| a_star(start, goal)                            |
|   -> A* Search                                 |
|                                                |
| manhattan(state)                               |
|   -> Manhattan-distance heuristic              |
|                                                |
| benchmark(func), main()                        |
|   -> profiling and program execution           |
+------------------------------------------------+
```

## 6. Design Decisions

The architecture separates input, search, heuristic calculation, memory and output so BFS and A* can share the same puzzle representation. Manhattan distance is isolated so the heuristic can be changed without redesigning the search engine. The modular structure also makes it easier to add other AI search algorithms later.

## 7. AI Contribution Note

- **AI tools used:** ChatGPT
- **What AI helped with:** Understanding the C4 structure, organizing the architecture, and improving report wording and diagram layout.
- **What I did myself:** I used and understood the BFS/A* implementation, ran the profiling experiment, checked the results, and prepared the final submission.

## 8. Conclusion

This SLE showed how an AI search program can be described at four architectural levels: context, container, component and code. The C4 model made the responsibilities of the 8-Puzzle Solver clearer and showed how BFS and A* fit into the same architecture. It also provides a structured foundation for extending the solver with additional search strategies.
