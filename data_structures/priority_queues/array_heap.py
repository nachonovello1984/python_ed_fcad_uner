from typing import Any, Tuple
from .priority_queue_base import PriorityQueueBase

class ArrayHeap(PriorityQueueBase):
    """ Implementa una cola de prioridad mínima con un heap binario."""
    
    #########################################################################
    #							MÉTODOS PÚBLICOS
    #########################################################################
    
    def __init__(self) -> None:
        """Crea un nuevo Heap"""
        self._data = []
        
    def __repr__(self) -> str:
        """Convierte en un string todos los nodos del heap.

        Returns:
            str: concatena en único string todos los nodos.
        """
        if self.is_empty():
            return "ArrayHeap()"
        
        return f"ArrayHeap({', '.join(list(str(x) for x in self._data))})"
    
    def __str__(self) -> str:
        """Ídem __repr__().

        Returns:
            str: string formado por la concatenación de todos los ítems del heap.
        """
        return repr(self)

    def __len__(self) -> int:
        """Devuelve la cantidad de nodos de la estructura.

		Returns:
			int: _description_
		"""
        return len(self._data)

    def is_empty(self) -> bool:
        """Indica si la estructura está vacía.

		Returns:
			bool: True si está vacía. False, en caso contrario.
		"""
        return len(self) == 0

    def add(self, key : Any, value: Any) -> None:
        """Agrega un nodo al Heap y lo deja en la posición definitiva aplicando rotaciones si corresponden.
  
		Args:
			key (Any): clave del nodo.
			value (Any): valor del nodo.
		"""
        self._data.append(self._Item(key, value)) # _Item es la clase definida en PriorityQueueBase
        self._upheap(len(self._data) - 1)  #El nuevo nodo es hoja y hay que dejarlo ordenado.

    def min(self) -> Tuple[Any, Any]:
        """Devuelve sin quitar el elemento ubicado en la raiz del heap.
  
		Raises:
			Exception: arroja excepción si la estructura está vacía.
   
   		Returns:
			Tuple[Any, Any]: retorna una tupla formada por la clave y valor del nodo.

		"""
        if self.is_empty():
            raise Exception("Heap vacío. No se puede continuar.")

        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self) -> Tuple[Any, Any]:
        """Quita el nodo con menor valor de clave.

        Returns:
			Tuple[Any, Any]: retorna una tupla formada por la clave y valor del nodo.
        
        Raises:
			Exception: Arroja excepción si la estructura está vacía.
		"""
        if self.is_empty():
            raise Exception("Priority queue is empty.")

        self._swap(0, len(self._data) - 1)  # Pone el mínimo valor al final de la lista.
        item = self._data.pop()  # Quita el valor final de la lista.
        self._downheap(0)  # Corrige el orden desde la raíz.

        return (item._key, item._value)
    
    #########################################################################
    #							MÉTODOS NO PÚBLICOS
    #########################################################################
    def _parent(self, j: int) -> int:
        """Devuelve el índice correspondiente al padre de un nodo.

		Args:
				j (int): índice del nodo del que se busca su padre.

		Returns:
			int: devuelve el índice del padre del nodo
		"""
        return (j - 1) // 2

    def _left(self, j: int) -> int:
        """Devuelve el índice correspondiente al hijo izquierdo del nodo en la posición j.

		Args:
			j (int): índice del nodo del que se busca su hijo izquierdo.

		Returns:
			int: devuelve el índice del hijo izquierdo del nodo en j.
		"""
        return 2 * j + 1

    def _right(self, j: int) -> int:
        """Devuelve el índice correspondiente al hijo derecho del nodo en la posición j

        Args:
        	j (int): índice del nodo del que se busca su hijo derecho.

        Returns:
        	int: devuelve el índice del hijo derecho del nodo en j.
        """
        return 2 * j + 2

    def _has_left(self, j: int) -> bool:
        """Indica si el nodo j tiene un hijo izquierdo

		Args:
			j (int): El nodo del que se busca saber si tiene hijo izquierdo

		Returns:
			bool: True si tiene hijo izquierdo, False en caso contrario.
		"""
        return self._left(j) < len(self._data)

    def _has_right(self, j: int) -> bool:
        """Indica si el nodo j tiene un hijo derecho.

		Args:
			j (int): El nodo del que se busca saber si tiene hijo derecho.

		Returns:
			bool: True si tiene hijo derecho, False en caso contrario.
		"""
        return self._right(j) < len(self._data) 

    def _swap(self, i: int, j: int) -> None:
        """Intercambia los elementos de los índices i y j del array.

		Args:
			i (int): primera posición.
			j (int): segunda posición.
		"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j: int) -> None:
        """En sentido ascendente intercambia los valores de los nodos para dejar en condición de heap la estructura.

		Args:
			j (int): nodo desde donde se inicia control/intercambio.
		"""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j: int) -> None:
        """En sentido descendente intercambia los nodos para que la estructura esté en condición de heap.

		Args:
			j (int): nodo desde donde se inicia control/intercambio.
		"""

        if self._has_left(j): # si el nodo tiene hijo izquierdo
            left = self._left(j)
            small_child = left  # lo guardo como valor más pequeño.
            
            if self._has_right(j): # si tiene hijo derecho
                right = self._right(j)
                if self._data[right] < self._data[left]: # si el derecho es menor que el izquierdo.
                    small_child = right
            
            if self._data[small_child] < self._data[j]: # si el menor es menor que el actual.
                self._swap(j, small_child) # Intercambio valores
                self._downheap(small_child)  # Continúo hacia abajo.

    
