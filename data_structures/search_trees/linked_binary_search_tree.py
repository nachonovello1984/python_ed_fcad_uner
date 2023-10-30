from ..trees import BinaryTreeNode
from ..trees import LinkedBinaryTree
from typing import Tuple, Any, Optional

class LinkedBinarySearchTree(LinkedBinaryTree):

    def add_left_child(self, parent: Optional[BinaryTreeNode], new_node: BinaryTreeNode) -> None:
        """ Método no permitido ya que no aplica a la definición del tipo

        Args:
            parent (Optional[BinaryTreeNode]): 
            new_node (BinaryTreeNode): 

        Raises:
            NotImplementedError: Siempre arroja excepción porque no es válido para el tipo de implementación.
        """
        raise NotImplementedError("Este método no está permitido en LinkedBinarySearchTree.")
    
    def add_right_child(self, parent: Optional[BinaryTreeNode], new_node: BinaryTreeNode) -> None:
        """ Método no permitido ya que no aplica a la definición del tipo

        Args:
            parent (Optional[BinaryTreeNode]): 
            new_node (BinaryTreeNode): 

        Raises:
            NotImplementedError: Siempre arroja excepción porque no es válido para el tipo de implementación.
        """
        raise NotImplementedError("Este método no está permitido en LinkedBinarySearchTree.")


    def remove(self, node: BinaryTreeNode) -> None:
        """ Método no permitido ya que no aplica a la definición del tipo

        Args:
            node (BinaryTreeNode): 

        Raises:
            NotImplementedError: Siempre arroja excepción porque no es válido para el tipo de implementación.
        """
        raise NotImplementedError("Este método no está permitido en LinkedBinarySearchTree.")

    def __contains__(self, element: Any) -> bool:
       res, _, _ = self._search(None, self._root, BinaryTreeNode(element))
       return res

    def add_element(self, element: Any) -> None:
        new_node = BinaryTreeNode(element)
        if self.is_empty():
            self._root = new_node
        else:
            res, parent, _ = self._search(None, self._root, new_node)
            if res:
                raise ValueError("Ya existe un elemento con igual clave en el árbol")

            if new_node.element < parent.element:
                parent.left_child = new_node
            else:
                parent.right_child = new_node
        
        self._size += 1 

    def remove_element(self, element: Any) -> None:
        res, _, eliminar = self._search(None, self._root, BinaryTreeNode(element))
        
        if not res:
            raise ValueError("No existe un nodo con valor de clave igual al pasado por parámetro.")
        
        super().remove(eliminar)

    #########################################################################
    #							MÉTODOS NO PÚBLICOS
    #########################################################################        
            
    def _search(self, parent: Optional[BinaryTreeNode], current: BinaryTreeNode, search: BinaryTreeNode) -> Tuple[bool, Optional[BinaryTreeNode], Optional[BinaryTreeNode]]:
        if current is None:
            return (False, parent, current)

        if search.element == current.element:
            return (True, parent, current)
        
        if search.element < current.element:
            return self._search(current, current.left_child, search)

        if search.element > current.element:
            return self._search(current, current.right_child, search)

