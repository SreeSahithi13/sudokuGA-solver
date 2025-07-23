# 🧠 Sudoku Solver using Genetic Algorithm

This project implements a Sudoku puzzle solver using a Genetic Algorithm (GA). It aims to fill the empty cells of a 9x9 Sudoku grid in a way that satisfies all Sudoku constraints.

## 📌 Features

- Solves standard 9x9 Sudoku puzzles using Genetic Algorithms
- Includes selection, crossover, and mutation operators
- Fitness function minimizes conflicts in columns and 3x3 subgrids
- Automatically stops when a valid solution is found or generation limit is reached

## 🛠 Tools and Technologies

- **Python 3.x**
- Built-in libraries: `random`, `copy`

## 📋 How It Works

1. **Initialization**: Generate a population of valid Sudoku boards, filling blank cells randomly without row duplicates.
2. **Fitness Function**: Calculates the number of conflicts in columns and 3x3 subgrids.
3. **Selection**: Uses tournament selection to pick parents for reproduction.
4. **Crossover**: Combines rows from two parents to create a child.
5. **Mutation**: Swaps two non-fixed values in a row to maintain diversity.
6. **Evolution**: Repeats for multiple generations to converge toward a solution.

## 🧪 Sample Puzzle (0 = blank cell)

