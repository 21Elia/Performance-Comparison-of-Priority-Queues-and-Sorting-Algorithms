# Performance Comparison: Priority Queues and Sorting Algorithms.
This repository contains a project developed for an Algorithms & Data Structures Course exam, which consists of a dual analysis:
  - **Sorting Algorithm Comparison**: features a benchmarking of Insertion Sort and Merge Sort
  - **Priority Queue Comparison**: Benchmarking three different Priority Queue implementations (Heap, Sorted List, Unsorted List) based on the asymptotic complexity of their operations.

The goal is to test and validate theoretical time and space complexities against empirical data across varying input sizes.

## Instructions

To run this analysis locally, you need Python 3 and the specified libraries.

Ensure you have the following Python libraries installed:

```
pip install pandas matplotlib
```

The project contains several files:

- `sorting_comparison.ipynb`: Jupyter Notebook with the full analysis, charts, and conclusions for the sorting algorithms.
- `tests.py`:  Execution script that runs tests and generates the comparison data/plots for the Priority Queues.
- `heap_priority_queue.py`: Max-Heap implementation of the Priority Queue.
- `sorted_list_priority_queue.py` Linked List implementation where keys are kept sorted. 
- `unsorted_list_priority_queue.py` Linked List implementation where keys are appended to the tail the list.
- `report.pdf` / `report.zip` Detailed theoretical analysis, methodology, code documentation, and results for the Priority Queue comparison.


## How to run

1. Sorting Analysis: open and run all cells in sorting_comparison.ipynb.
2. Priority Queue Analysis: ensure you are in the right directory and execute the `tests.py` script (it will generate the graphs and print the tables).
```
python tests.py
```
