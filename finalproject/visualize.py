from graphviz import Digraph

def visualize_bst(root):
    dot = Digraph()
    
    def add_nodes_edges(node):
        if not node:
            return
        dot.node(str(node.id), f'{node.name}\nID: {node.id}', style='filled', fillcolor='orange', color='black')
        if node.left:
            dot.edge(str(node.id), str(node.left.id))
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(str(node.id), str(node.right.id))
            add_nodes_edges(node.right)
 
    add_nodes_edges(root)
    dot.render('bst_graph', format='png', cleanup=True)
    print("📄 BST graph saved as bst_graph.png")

def visualize_heap(heap_list):
    dot = Digraph()
    for i in range(1, len(heap_list)):
        node = heap_list[i]
        dot.node(str(node.id), f'ID: {node.id}\nPriority: {node.priority}', style='filled', fillcolor='green', color='black')
        if 2 * i < len(heap_list):
            dot.edge(str(node.id), str(heap_list[2 * i].id))
        if 2 * i + 1 < len(heap_list):
            dot.edge(str(node.id), str(heap_list[2 * i + 1].id))
    
    dot.render('heap_graph', format='png', cleanup=True)
    print("📄 MaxHeap graph saved as heap_graph.png")