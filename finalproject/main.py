from binarySearchTree import BST
from maxHeap import MaxHeap
from visualize import visualize_bst, visualize_heap

def print_menu():
    print("\n=== Request Management System ===")
    print("1. Add new request")
    print("2. Process highest priority request")
    print("3. Search request by ID")
    print("4. Update request priority")
    print("5. Delete request")
    print("6. Print all requests in BST")
    print("7. Print all requests in Heap")
    print("8. Visualize BST and Heap")
    print("9. Exit")
    print("===============================")

def main():
    bst = BST()
    max_heap = MaxHeap()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            id = int(input("Enter request ID: "))
            name = input("Enter request name: ")
            priority = int(input("Enter request priority: "))
            
            bst.insertRequest(id, name)
            max_heap.insertHeap(id, priority)
            print("Request added successfully!")
            
        elif choice == '2':
            if max_heap.isEmptyHeap():
                print("No requests to process!")
            else:
                request_id = max_heap.processHighestPriorityRequest(bst)
                print(f"Processing request with ID: {request_id}")
                
        elif choice == '3':
            id = int(input("Enter request ID to search: "))
            node = bst.searchRequest(id)
            if node:
                print(f"Request found - id: {node.id}, name: {node.name}")
            else:
                print("Request not found!")
                
        elif choice == '4':
            if max_heap.isEmptyHeap():
                print("No requests to update!")
            else:
                id = int(input("Enter request ID: "))
                new_priority = int(input("Enter new priority: "))
                max_heap.increasePriority(id, new_priority)
                print("Priority updated successfully!")
                
        elif choice == '5':
            id = int(input("Enter request ID to delete: "))
            if bst.searchRequest(id):
                bst.deleteRequest(id)
                print("Request deleted successfully!")
            else:
                print("request not found.\n")
                
        elif choice == '6':
            print("\nRequests in BST (Pre-order traversal):")
            bst.printBST()
                
        elif choice == '7':
            print("\nRequests in Max Heap (Level-order):")
            max_heap.printMaxHeap()

        elif choice == '8':
            visualize_bst(bst.root)
            visualize_heap(max_heap.heap) 

        elif choice == '9':
            print("Thank you for using the Request Management System!")
            break
                
        else:
            print("Invalid choice! Please try again.")
            
if __name__ == "__main__":
    main()