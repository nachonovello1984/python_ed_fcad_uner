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


# print(f"{' RECORRIDO EN PREORDEN ':*^60}")

# for item in tree.preorder_traversal():
#     print(item, end=", ")
    
# print("")

# print(f"{' QUITANDO NODOS ':*^60}")

# tree.remove(node_20)
# print("tree.remove(20):", tree)

# tree.remove(node_15)
# print("tree.remove(15):", tree)

# tree.remove(node_25)
# print("tree.remove(25):", tree)


# nodo_a = BinaryTreeNode('A')
# nodo_b = BinaryTreeNode('B')
# nodo_c = BinaryTreeNode('C')
# nodo_d = BinaryTreeNode('D')
# nodo_f = BinaryTreeNode('F')
# nodo_g = BinaryTreeNode('G')
# nodo_h = BinaryTreeNode('H')
# nodo_i = BinaryTreeNode('I')
# nodo_k = BinaryTreeNode('K')
# nodo_m = BinaryTreeNode('M')
# nodo_n = BinaryTreeNode('N')

# arbol_letras = LinkedBinaryTree()
# arbol_letras.add_left_child(None, nodo_a)
# arbol_letras.add_left_child(nodo_a, nodo_b)
# arbol_letras.add_right_child(nodo_a, nodo_f)
# arbol_letras.add_left_child(nodo_b, nodo_c)


# print(f"{' RECORRIDO EN INORDEN ':*^60}")

# for item in arbol_letras.inorder_traversal():
#     print(item, end=", ")
    
# print("")