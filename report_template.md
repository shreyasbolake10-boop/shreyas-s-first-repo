# SLE-2: Profiling Report

**Course:** 02AML204 – Introduction to Artificial Intelligence

**PRN:** ____________________  
**Name:** ____________________  
**Division:** A / B  
**Date:** ____________________  
**GitHub Link:** ____________________

## 1. Algorithms / Versions Profiled

- **Algorithm A:** Breadth-First Search (BFS)
- **Algorithm B:** A* Search with Manhattan-distance heuristic
- **Problem used:** 8-Puzzle

## 2. Profiling Method

- **Tool used:** Python `timeit` module + manual node counter
- **How I measured:** Both algorithms were run on the same start and goal states. Each was executed 5 times. Average execution time and nodes expanded were recorded.
- **Number of runs:** 5

## 3. Results

Replace the blanks using your own output from `python profiling.py`.

| Metric | BFS | A* |
|---|---:|---:|
| Avg. Time (ms) | ____ | ____ |
| Nodes Expanded | ____ | ____ |
| Solution Depth | ____ | ____ |

### Short observation

Write 2–3 lines describing the measured differences.

## 4. Justification & Analysis

BFS explores states level by level without a heuristic. A* uses Manhattan distance to prioritize states that appear closer to the goal. Use your measured time and node counts as the evidence for the comparison. If A* expands fewer nodes, explain that the heuristic reduces unnecessary exploration. Mention that exact timing depends on hardware, Python version, and system load.

## 5. AI Contribution Note

- **AI tools used:** ChatGPT / GitHub Copilot (as applicable)
- **What AI helped with:** Initial code structure, profiling setup, explanation, and report formatting.
- **What I did myself:** I ran the experiment, collected the measurements, checked the results, and wrote the final observations.

## 6. Conclusion

State what you learned about empirical profiling, execution time, node expansion, and the practical effect of heuristic search.

> **Important:** Use your own measured values. Do not submit placeholder or invented numbers.
