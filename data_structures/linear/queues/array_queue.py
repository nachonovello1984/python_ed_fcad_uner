from typing import Any, List

class ArrayQueue:
    """Implementación de Cola (E.D. tipo FIFO) utilizando una lista de Python para almacenar elementos."""
    
    DEFAULT_CAPACITY : int = 10
    
    def __init__(self) -> None:
        """Crea una cola vacía"""
        self._data : List[Any] = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front: int = 0
        self._back: int = -1
        self._size : int = 0
    
    def __len__(self) -> int:
        """Devuelve el número de elementos en la estructura.

        Returns:
            int: entero que indica la cantidad actual de elementos almacenados en la estructura. 
        """
        return self._size
    
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos almacenados en la fila/cola.

        Returns:
            str: string con todos los elementos que contiene la estructura.
        """
        #Convierto todos los elementos en la lista a str.
        str_lista = [str(elem) for elem in self._data if elem is not None]
                
        return "ArrayQueue(" + ", ".join(str_lista) + ")"
        
    def is_empty(self) -> bool:
        """Indica si la cola está vacía

        Returns:
            bool: True si la cola está vacía, False en caso contrario
        """
        return self._size == 0
    
    def is_full(self) -> bool:
        """Indica si la estructura está llena.

        Returns:
            bool: True si se llenó la fila, caso contrario False
        """
        return self._size == len(self._data)
    
    def first(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente de la cola."

        Raises:
            Exception: Arroja excepción si la estructura está vacía.

        Returns:
            Any: Devuelve el elemento más antigüo en orden de inserción.
        """
        
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar")
        
        return self._data[self._front]
    
    def dequeue(self) -> Any:
        """Remueve y devuelve el primer elemento de la cola.

        Returns:
            Any: valor ubicado en el frente de la estructura.
        """
        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        resultado = self._data[self._front]
        self._data[self._front] = None
        self._front = self._incrementar(self._front)
        self._size -= 1
        return resultado
    
    def enqueue(self, elem: Any) -> None:
        """Agrega un elemento al final de la estructura.

        Args:
            elem (Any): Nuevo elemento al final de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está llena.
        """
        if self.is_full():
            raise Exception ("Estructura llena. No se puede continuar")
        
        self._back = self._incrementar(self._back)
        self._data[self._back] = elem
        self._size += 1
    
    def _incrementar(self, x : int) -> int:
        return (x + 1) % len(self._data)