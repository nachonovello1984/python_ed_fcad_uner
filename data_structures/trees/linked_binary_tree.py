from typing import Any, Iterable, Optional, Tuple, List
from ..linear.queues import LinkedQueue
from .binary_tree_node import BinaryTreeNode


class LinkedBinaryTree:
    """Implementación enlazada de Árbol Binario."""

    #########################################################################
    # 							MÉTODOS PÚBLICOS
    #########################################################################

    def __init__(self) -> None:
        """Crea un nuevo árbol binario vacío."""
        self._root: Optional[BinaryTreeNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        """Cantidad actual de nodos en la estructura.

        Returns:
            int: Número de nodos en la estructura.
        """
        return self._size

    def __repr__(self) -> str:
        """Convierte en un string todos los nodos del árbol.

        Returns:
            str: concatena en único string todos los nodos.
        """
        if self.is_empty():
            return "BinaryTree()"

        # Si la estructura no está vacía => uso un iterador para acceder a los elementos.
        res = ""

        for element in self.__iter__():
            res += f"{str(element)}, "

        res = res[:-2]

        return f"BinaryTree({res})"

    def __str__(self) -> str:
        """Ídem __repr__().

        Returns:
            str: string formado por la concatenación de todos los nodos.
        """
        return repr(self)

    def __iter__(self) -> Iterable[Any]:
        """Itera por niveles la estructura.

        Yields
            Iterator[Iterable[Any]]: yield del elemento de todos los nodos que va visitando.
        """
        queue = LinkedQueue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            current = queue.first()

            yield current.element

            if current.left_child:
                queue.enqueue(current.left_child)

            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()

    def is_empty(self) -> bool:
        """Indica si la estructura está vacía.

        Returns:
            bool: True si la cantidad de elementos es 0. False en caso contrario.
        """
        return self._size == 0

    def root(self) -> Any:
        """Devuelve el elemento de la raíz del árbol.

        Returns:
            Any: carga útil de la raíz.
        """
        if self.is_empty():
            return None

        return self._root.element  # type: ignore

    def add_root(self, new_node: BinaryTreeNode) -> None:
        """Establece el nodo pasado por parámetro como raíz del árbol.

        Args:
            new_node (BinaryTreeNode): nodo que se convertirá en raíz del árbol.

        Raises:
            Exception: arroja excepción cuando se intenta establecer una raíz para un árbol no vacío.
        """
        if not self.is_empty():
            raise Exception(
                "El árbol no está vacío. No se puede definir una nueva raíz"
            )

        self._root = new_node
        self._size += 1

    def add_left_child(self, parent: Optional[BinaryTreeNode], new_node: BinaryTreeNode) -> None:
        """Agrega un hijo izquierdo al nodo especificado como padre.

        Args:
            parent (Optional[BinaryTreeNode]): padre del nodo a insertar.
            new_node (BinaryTreeNode): nodo a insertar.
        """
        self._add_child(True, parent, new_node)

    def add_right_child(self, parent: Optional[BinaryTreeNode], new_node: BinaryTreeNode) -> None:
        """Agrega un hijo derecho al nodo especificado como padre.

        Args:
            parent (Optional[BinaryTreeNode]): padre del nodo a insertar.
            new_node (BinaryTreeNode): nodo a insertar.
        """
        self._add_child(False, parent, new_node)

    def remove(self, node: BinaryTreeNode) -> None:
        """Quita del árbol el nodo pasado por parámetro.

        Args:
            node (BinaryTreeNode): nodo que se quita de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía o si el nodo no pertenece al árbol.
        """
        if self.is_empty():
            raise Exception("Estructura vacía. La operación no se puede llevar a cabo.")

        if not self._contains(node):
            raise Exception(
                "El nodo pasado por parámetro no pertenece a la estructura."
            )

        parent = self._search_parent(node)

        # Si no tiene nodos hijos..
        if node.children_count == 0:
            # Si el nodo a eliminar tiene padre
            if parent:
                # Si el nodo es hijo izquierdo...
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:  # Si el nodo a eliminar no tiene padre
                self._root = None

        elif node.children_count == 1:  # Si el nodo a eliminar tiene 1 hijo...
            # Si el nodo a eliminar tiene padre...
            if parent:
                # Si el nodo es hijo izquierdo...
                if parent.left_child == node:

                    # Si tiene hijo izquierdo...
                    if node.left_child:
                        parent.left_child = node.left_child
                    else:
                        parent.left_child = node.right_child
                else:  # Si el nodo es hijo derecho...

                    # Si tiene hijo izquierdo...
                    if node.left_child:
                        parent.right_child = node.left_child
                    else:
                        parent.right_child = node.right_child
            else:  # Si el nodo a eliminar no tiene padre..
                # Si el nodo a eliminar es hijo izquierdo...
                if node.left_child:
                    self._root = node.left_child
                else:
                    self._root = node.right_child
        else:
            # Si el nodo a eliminar tiene dos hijos
            replace_node = self._search_replace(node)
            self.remove(replace_node)  # type: ignore
            node.element = replace_node.element  # type: ignore

        self._size -= 1

    def preorder_traversal(self) -> Iterable[Any]:
        """Recorrido en preorden del árbol.

        Returns:
            Iterable[Any]: Devuelve un iterador que comienza por el nodo raíz.
        """
        return self._preorder_traversal(self._root)

    def inorder_traversal(self) -> Iterable[Any]:
        return self._inorder_traversal(self._root)

    def vertical_str(self) -> str:

        if self.is_empty():
            raise Exception("No se puuede llevar a cabo esta operación si el árbol está vacío.")

        return self._vertical_str(self._root)

    #########################################################################
    # 							MÉTODOS NO PÚBLICOS
    #########################################################################

    def _vertical_str(self, nodo, level=0, space=8) -> str:

        if nodo is None:
            return ""

        space += 8

        # Imprimir primero el subárbol derecho
        res = self._vertical_str(nodo.right_child, level + 1, space)

        # Imprimir el nodo actual después del espacio adecuado
        res += "\n"
        res += " " * (space - 8) + str(nodo.element)

        # Imprimir el subárbol izquierdo
        res += self._vertical_str(nodo.left_child, level + 1, space)

        return res

    def _preorder_traversal(self, node: Optional[BinaryTreeNode]):
        """Realiza un recorrido en preorden desde el node.

        Args:
            node (Optional[BinaryTreeNode]): nodo desde donde inicia el recorrido en preorden.

        Yields:
            Any: Devuelve el elemento de cada nodo.
        """
        if node:
            yield node.element

            yield from self._preorder_traversal(node.left_child)
            yield from self._preorder_traversal(node.right_child)

    def _inorder_traversal(self, node: Optional[BinaryTreeNode]) -> Iterable[Any]:

        if node:
            yield from self._preorder_traversal(node.left_child)

            yield node.element

            yield from self._preorder_traversal(node.right_child)

    def _postorder_traversal(self, node: Optional[BinaryTreeNode]) -> Iterable[Any]:

        if node:
            yield from self._preorder_traversal(node.left_child)

            yield from self._preorder_traversal(node.right_child)

            yield node.element

    def _contains_rec(self, current: BinaryTreeNode, search: BinaryTreeNode) -> bool:
        """Verifica recursivamente si un nodo pertenece a la estructura.

        Args:
            current (BinaryTreeNode): nodo desde donde comienza la búsqueda.
            search (BinaryTreeNode): nodo buscado.

        Returns:
            bool: indica si el nodo search forma parte del árbol.
        """
        res = False
        if current == search:
            res = True
        else:
            if current.left_child:
                res = self._contains_rec(current.left_child, search)

            if not res and current.right_child:
                res = self._contains_rec(current.right_child, search)

        return res

    def _contains(self, node: BinaryTreeNode) -> bool:
        """Indica si el nodo pasado por parámetro pertenece a la estructura.

        Args:
            node (BinaryTreeNode): nodo a buscar.

        Returns:
            bool: True si se encuentra. False en caso contrario.
        """
        if self._root is None:
            return False

        return self._contains_rec(self._root, node)

    def _add_child(
        self, is_left: bool, parent: Optional[BinaryTreeNode], new_node: BinaryTreeNode
    ) -> None:
        """Agrega un new_node como hijo de parent.

        Args:
            is_left (bool): indica si new_node es hijo izquierdo o derecho de parent.
            parent (Optional[BinaryTreeNode]): nodo padre.
            new_node (BinaryTreeNode): nuevo nodo a agregar.

        Raises:
            Exception: arroja excepciones si los parámetros son incorrectos.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si el árbol está vacío.")

        if not parent:
            raise Exception(
                "No se puede agregar un nodo sin padre si la estructura está vacía."
            )

        if not self._contains(parent):
            raise Exception("El nodo padre no pertenece al árbol")

        if self._contains(new_node):
            raise Exception("El nuevo nodo ya pertenece al árbol")

        if parent.left_child and is_left:
            raise Exception("El nodo padre ya tiene un hijo izquierdo.")

        if parent.right_child and not is_left:
            raise Exception("El nodo padre ya tiene un hijo derecho.")

        if is_left:
            parent.left_child = new_node
        else:
            parent.right_child = new_node

        self._size += 1

    def _search_parent(self, search: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        """Busca el padre del nodo search.

        Args:
            search (BinaryTreeNode): nodo del que se busca su padre.

        Returns:
            Optional[BinaryTreeNode]: nodo padre o None en caso que search sea raíz.
        """
        # Agrego la raíz a una cola
        queue = LinkedQueue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            current = queue.first()

            # Si current tiene un hijo izquierdo...
            if current.left_child:
                # Si el hijoIzquierdo es el nodo del que estoy buscando el padre...
                if current.left_child == search:
                    return current

                queue.enqueue(current.left_child)

            # Si nodoActual tiene un hijo derecho...
            if current.right_child:
                # Si el hijoDerecho es el nodo del que estoy  buscando el padre...
                if current.right_child == search:
                    return current

                queue.enqueue(current.right_child)

            queue.dequeue()

        return None

    def _search_replace(self, node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        """Busca como reemplazo el nodo ubicado más a la izquierda del subárbol derecho de node.

        Args:
            node (BinaryTreeNode): nodo desde donde comenzar la búsqueda.

        Returns:
            Optional[BinaryTreeNode]: Nodo más a la izquierda del subárbol derecho de node.
        """
        actual = node.right_child

        if actual is None:
            return actual

        while actual.left_child:
            actual = actual.left_child

        return actual
