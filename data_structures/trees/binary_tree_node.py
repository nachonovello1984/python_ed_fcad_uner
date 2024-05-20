from typing import Any, Optional

class BinaryTreeNode:
    """Nodo árbol binario con representación por enlaces."""
    
    def __init__(self, element : Any, left_child: Optional['BinaryTreeNode'] = None, right_child: Optional['BinaryTreeNode'] = None) -> None:
        """Crea un nuevo nodo binario.

        Args:
            element (Any): carga útil del nodo.
            left_child (Optional['BinaryTreeNode'], optional): referencia al hijo izquierdo. Defaults to None.
            right_child (Optional['BinaryTreeNode'], optional): referencia al hijo derecho. Defaults to None.
        """
        self.element = element
        self.left_child = left_child
        self.right_child = right_child
    
    def __eq__(self, other: 'BinaryTreeNode') -> bool:
        """Verifica si un nodo es igual a otro.

        Args:
            other (BinaryTreeNode): nodo para comprar

        Returns:
            bool: True si el elemento de los dos nodos es igual. False en caso contrario.
        """
        if not isinstance(other, BinaryTreeNode):
            return False
        
        return self.element == other.element
        
    def __str__(self) -> str:
        """Devuelve la representación en str del nodo.

        Returns:
            str: concatena en un str el elemento del nodo.
        """
        return f"[{self.element}]"

    @property  
    def children_count(self) -> int:
        """Devuelve la cantidad de hijos del nodo.

        Returns:
            int: Número de hijos del nodo.
        """
        return (1 if self.left_child else 0) + (1 if self.right_child else 0)