from data_structures import LinkedBinaryTree, BinaryTreeNode

node_25 = BinaryTreeNode(25)
node_15 = BinaryTreeNode(15)
node_35 = BinaryTreeNode(35)
node_20 = BinaryTreeNode(20)

tree = LinkedBinaryTree()

tree.add_left_child(None, node_25)
print(tree)
tree.add_left_child(node_25, node_15)
print(tree)
tree.add_right_child(node_25, node_35)
print(tree)
tree.add_left_child(node_15, BinaryTreeNode(10))
tree.add_right_child(node_15, node_20)

print(f"{' ÁRBOL COMPLETO ':*^60}")
print(tree)

print(f"{' RECORRIDO EN PREORDEN ':*^60}")

for preorden_item in tree.preorder_traversal():
    print(preorden_item, end=", ")
    
print("")

print(f"{' QUITANDO NODOS ':*^60}")

tree.remove(node_20)
print("tree.remove(20):", tree)

tree.remove(node_15)
print("tree.remove(15):", tree)

tree.remove(node_25)
print("tree.remove(25):", tree)

