from data_structures import LinkedBinarySearchTree
from random import randrange

arbol = LinkedBinarySearchTree()
arbol.add_element("B")
arbol.add_element("C")
arbol.add_element("D")
arbol.add_element("A")

print(f"árbol completo: {arbol}")


set = set()
set.add(50)
set.add(100)

for i in range(1, 11):
    set.add(randrange(1, 100))

arbol = LinkedBinarySearchTree()
for item in set:
    arbol.add_element(item)


print(f"árbol completo: {arbol}")

if 50 in arbol:
    print("50 existe en árbol")
else:
    print("50 no existe en árbol")

if 100 in arbol:
    print("100 existe en árbol")
else:
    print("100 no existe en árbol")
