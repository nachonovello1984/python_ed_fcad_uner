from typing import Any, Optional
from ..list_node import ListNode

class LinkedStack:
    """Implementación de Pila (E.D. tipo LIFO) utilizando representación por enlaces."""
    def __init__(self) -> None:
        """Crea una pila vacía"""
        self._head : Optional[ListNode] = None
        self._size : int = 0

    def __len__(self) -> int:
        """Devuelve el número de elementos en la Pila.

        Returns:
            int: entero que indica la cantidad actual de elementos almacenados en la pila. 
        """
        return self._size
    
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos almacenados en la pila

        Returns:
            str: string con todos los elementos que contiene la pila.
        """
        #Si la estructura está vacía => retorno siempre lo mismo.
        if self.is_empty():
            return "LinkedStack()"
        
        resultado = "" # inicializo resultado con el string vacío

        #Me quedo en actual con el elemento ubicado en el tope     
        actual = self._head
        while actual:
            # proceso el elemento del nodo actual
            resultado += str(actual.element) + ", "
            # establezco el siguiente nodo como nodo actual
            actual = actual.next 
        
        #Quito los dos últimos caracteres del string    
        resultado = resultado[:len(resultado)-2]
        
        return f"LinkedStack({resultado})"
    
    def is_empty(self) -> bool:
        """Indica si la pila está vacía

        Returns:
            bool: True si la pila está vacía, False en caso contrario
        """
        return self._size == 0
    
    def push(self, elem: Any) -> None:
        """Agrega el elemento elem en el tope de la pila.

        Args:
            elem (Any): Nuevo elemento que se va agregar a la pila.
        """
        #nuevo_tope tiene como siguiente al actual tope (self._head)
        nuevo_tope = ListNode(elem, self._head)
        
        #hago a nuevo_tope el nuevo nodo cabecera o head
        self._head = nuevo_tope
        self._size += 1
        
    def top(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        return self._head.element # type: ignore
        
    def pop(self) -> Any:
        """Quita y devuelve el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        #Dejo en resultado el valor a devolver.
        res = self._head.element # type: ignore
        
        #Hago tope al siguiente al tope.
        self._head = self._head.next # type: ignore
        self._size -= 1
        
        return res