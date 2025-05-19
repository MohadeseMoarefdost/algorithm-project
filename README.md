# Request Management System

A Python-based Request Management System that efficiently handles requests using a combination of Binary Search Tree (BST) and Max Heap data structures. The system provides a user-friendly interface for managing requests with different priorities.

## Features

- Add new requests with ID, name, and priority
- Process highest priority requests automatically
- Search requests by ID
- Update request priorities
- Delete requests
- Visualize both BST and Max Heap structures
- Print all requests in both BST and Heap formats

## Data Structures Used

### Binary Search Tree (BST)
- Efficient for searching and retrieving requests by ID
- Maintains sorted order of requests
- O(log n) average case for search, insert, and delete operations

### Max Heap
- Efficient for managing request priorities
- O(1) access to highest priority request
- O(log n) for insert and delete operations

## Requirements

- Python 3.x
- Graphviz (for visualization)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install required packages:
```bash
pip install graphviz
```

3. Install Graphviz:
   - Windows: Download and install from [Graphviz website](https://graphviz.org/download/)
   - Make sure to add Graphviz to your system's PATH

## Usage

Run the main program:
```bash
python main.py
```

### Menu Options

1. Add new request
2. Process highest priority request
3. Search request by ID
4. Update request priority
5. Delete request
6. Print all requests in BST
7. Print all requests in Heap
8. Visualize BST and Heap
9. Exit

## Visualization

The system generates two visualization files:
- `bst_graph.png`: Visual representation of the Binary Search Tree
- `heap_graph.png`: Visual representation of the Max Heap

## Project Structure

- `main.py`: Main program and user interface
- `binarySearchTree.py`: BST implementation
- `MaxHeap.py`: Max Heap implementation
- `visualize.py`: Visualization utilities
- `README.md`: Project documentation

## Contributing

Feel free to submit issues and enhancement requests!
