from typing import Any, Optional
from ..list_node import ListNode

class LinkedQueue:
    """Implementación de Cola (E.D. tipo FIFO) utilizando representación por enlaces."""
    
    def __init__(self) -> None:
        """Crea una cola vacía"""
        self._front: Optional[ListNode] = None
        self._back: Optional[ListNode] = None
        self._size: int = 0
    
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
        
        #Si la estructura está vacía => retorno siempre lo mismo.
        if self.is_empty():
            return "LinkedQueue()"
        
        resultado = "" # inicializo resultado con el string vacío

        #Me quedo en actual con el elemento ubicado en el frente
        actual = self._front
        while actual:
            # proceso el elemento del nodo actual
            resultado += str(actual.element) + ", "
            
            # establezco el siguiente nodo como nodo actual
            actual = actual.next 
        
        #Quito los dos últimos caracteres del string    
        resultado = resultado[:len(resultado)-2]
        
        return f"LinkedQueue({resultado})"
        
    def is_empty(self) -> bool:
        """Indica si la cola está vacía

        Returns:
            bool: True si la cola está vacía, False en caso contrario
        """
        return self._size == 0
    
    def is_full(self) -> bool:
        """Indica si la estructura está llena. 
        En esta implementación no hay limitante de tamaño.

        Returns:
            bool: siempre devuelve False. 
        """
        return False
    
    def first(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente de la cola."

        Raises:
            Exception: Arroja excepción si la estructura está vacía.

        Returns:
            Any: Devuelve el elemento más antigüo en orden de inserción.
        """
        
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar")
        
        return self._front.element # type: ignore
    
    def dequeue(self) -> Any:
        """Remueve y devuelve el primer elemento de la cola.

        Returns:
            Any: valor ubicado en el frente de la estructura.
        """
        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        res = self._front.element # type: ignore
        self._front = self._front.next # type: ignore
        self._size -= 1

        # Para cuando ya no queden elementos hago None _back
        if self._size == 0:
            self._back = None

        return res
    
    def enqueue(self, elem: Any) -> None:
        """Agrega un elemento al final de la estructura.

        Args:
            elem (Any): Nuevo elemento al final de la estructura.
        """
        nuevo_nodo = ListNode(elem, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo # type: ignore
            self._back = self._back.next # type: ignore
            
        self._size += 1