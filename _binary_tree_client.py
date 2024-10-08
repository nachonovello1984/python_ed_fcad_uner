from data_structures import LinkedBinaryTree, BinaryTreeNode

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_k = BinaryTreeNode('K')
nodo_m = BinaryTreeNode('M')
nodo_n = BinaryTreeNode('N')

arbol_letras = LinkedBinaryTree()
arbol_letras.add_root(nodo_a)
arbol_letras.add_left_child(nodo_a, nodo_b)
arbol_letras.add_left_child(nodo_b, nodo_c)
arbol_letras.add_right_child(nodo_b, nodo_d)

arbol_letras.add_right_child(nodo_a, nodo_f)
arbol_letras.add_left_child(nodo_f, nodo_g)
arbol_letras.add_left_child(nodo_g, nodo_h)
arbol_letras.add_right_child(nodo_g, nodo_i)

arbol_letras.add_right_child(nodo_f, nodo_k)
arbol_letras.add_left_child(nodo_k, nodo_m)
arbol_letras.add_right_child(nodo_k, nodo_n)

print()
print(f"{' ARBOL BINARIO STR ':*^60}")
print("str(arbol_letras):", arbol_letras)

print()
print(f"{' ARBOL BINARIO VERTICAL STR ':*^60}")
print(arbol_letras.vertical_str())

print(f"{' RECORRIDO POR NIVELES ':*^60}")
print(*[item for item in arbol_letras], sep=", ", end=".")  # type: ignore
print()

print(f"{' RECORRIDO EN PREORDEN ':*^60}")
for item in arbol_letras.preorder_traversal():
    print(item, end=", ")
print()


# print(f"{' RECORRIDO EN PREORDEN ':*^60}")
# print(*[item for item in arbol_letras.preorder_traversal()], sep=", ", end=".")  # type: ignore

# node_25 = BinaryTreeNode(25)
# node_15 = BinaryTreeNode(15)
# node_35 = BinaryTreeNode(35)
# node_20 = BinaryTreeNode(20)

# tree = LinkedBinaryTree()

# tree.add_left_child(None, node_25)
# print(tree)
# tree.add_left_child(node_25, node_15)
# print(tree)
# tree.add_right_child(node_25, node_35)
# print(tree)
# tree.add_left_child(node_15, BinaryTreeNode(10))
# tree.add_right_child(node_15, node_20)

# print(f"{' ÁRBOL COMPLETO ':*^60}")
# print(tree)


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

print(f"{' Graficar árbol con TKINTER ':*^60}")
import tkinter as tk

def draw_tree(canvas, node, x, y, x_offset, y_offset):
    if node is None:
        return

    # Dibujar las ramas y llamar recursivamente a los hijos
    if node.left_child:
        canvas.create_line(x, y, x - x_offset, y + y_offset)
        draw_tree(canvas, node.left_child, x - x_offset, y + y_offset, x_offset // 2, y_offset)
    
    if node.right_child:
        canvas.create_line(x, y, x + x_offset, y + y_offset)
        draw_tree(canvas, node.right_child, x + x_offset, y + y_offset, x_offset // 2, y_offset)

    # Dibujar el nodo actual
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill='lightblue')
    canvas.create_text(x, y, text=node.element, font=('Arial', 12))

root_window = tk.Tk()
root_window.title('Árbol Binario')
canvas = tk.Canvas(root_window, width=600, height=400, bg='white')
canvas.pack()

# Dibujar el árbol en el canvas
draw_tree(canvas, nodo_a, 300, 50, 100, 60)

root_window.mainloop()