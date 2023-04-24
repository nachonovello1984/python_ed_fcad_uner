from collections.abc import Sequence
from typing import TypeVar, Generic

T = TypeVar('T')

class ArrayStack(Generic[T]):
    
    """Implementación de Pila (E.D. tipo LIFO) utilizando una lista de Python para almacenar elementos."""
    def __init__(self) -> None:
        """Crea una pila vacía"""
        self._data: list[T] = [] 
    
    def __len__(self) -> int:
        """Devuelve el número de elementos en la Pila.

        Returns:
            int: entero que indica la cantidad actual de elementos almacenados en la pila. 
        """
        return len(self._data)
    
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos almacenados en la pila

        Returns:
            str: string con todos los elementos que contiene la pila.
        """
        #Convierto todos los elementos en la lista a str (en orden invertido).
        str_lista = [str(elem) for elem in self._data[::-1]]
                
        return "ArrayStack(" + ", ".join(str_lista) + ")"
    
    def is_empty(self) -> bool:
        """Indica si la pila está vacía

        Returns:
            bool: True si la pila está vacía, False en caso contrario
        """
        return len(self._data) == 0
    
    def push(self, elem: T) -> None:
        """Agrega el elemento elem en el tope de la pila.

        Args:
            elem (Any): Nuevo elemento que se va agregar a la pila.
        """
        self._data.append(elem) #Agrega elem al final de la lista.
        
    def top(self) -> T:
        """Devuelve (sin quitar) el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if self.is_empty():
            raise Exception("La pila está vacía. La operación no se puede llevar a cabo.")
        
        return self._data[-1] # Devuelve el último elemento de la lista.
    
    def pop(self) -> T:
        """Quita y devuelve el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("La pila está vacía")
        
        return self._data.pop() # Quita el último elemento de la lista.