# algorithm-project
# Request Management System using Binary Search Tree (BST) and MaxHeap

## 📌 Project Description
This project implements a **request management system** using two fundamental data structures:
- **Binary Search Tree (BST)** – for storing user requests by unique ID and name.
- **MaxHeap** – for prioritizing and processing requests based on priority values.

The system supports insertion, search, deletion, and processing of requests based on the highest priority.

---

## ⚙️ Data Structures Used

### 🔹 Binary Search Tree (BST)
Used to store requests by:
- `ID` (unique identifier)
- `Name` (user or task name)

**Operations:**
- `insertRequest(id, name)` – Inserts a new request into the BST.
- `searchRequest(id)` – Searches for a request by its ID.
- `deleteRequest(id)` – Deletes a request by ID.
- `printBST()` – Prints the BST in Pre-order traversal.
- `isEmptyBST()` – Checks if the BST is empty.
- `sizeBST()` – Counts the number of nodes in the BST.

---

### 🔹 MaxHeap
Used to manage request priorities based on:
- `ID`
- `Priority` (higher values have higher priority)

**Operations:**
- `insertHeap(id, priority)` – Inserts a request into the MaxHeap.
- `deleteMaxHeap()` – Removes the request with the highest priority.
- `processHighestPriorityRequest()` – Processes and removes the top-priority request from both MaxHeap and BST.
- `printMaxHeap()` – Prints MaxHeap in level-order traversal.
- `maxHeapify(index)` – Rebuilds the heap from a given index.
- `increasePriority(id, newPriority)` – Increases the priority of a specific request.
- `isEmptyHeap()` – Checks if the MaxHeap is empty.
- `sizeMaxHeap()` – Returns the number of elements in the MaxHeap.

---

## 🔄 System Workflow

### 1. Insert Request:
- Step 1: Store request ID and Name in BST.
- Step 2: Store the same request with ID and Priority in MaxHeap.

### 2. Search & Delete:
- You can search or delete any request using its ID from the BST.
- Deletion from MaxHeap requires locating the index and using `maxHeapify` to maintain heap order.

### 3. Process Requests by Priority:
- The request with the highest priority is removed from the MaxHeap.
- The corresponding request is also removed from the BST.

### 4. Increase Request Priority:
- You can increase the priority of a request using `increasePriority`.
- The heap will be restructured using `maxHeapify`.

---

## 🛠 Language & Tools
- **Language:** Python
- **Core Structures:** Separate classes for `BSTNode`, `HeapNode`, `BST`, and `MaxHeap`
- Ideal for task queues, service systems, request tracking, etc.

---

## 📁 Suggested Project Structure
