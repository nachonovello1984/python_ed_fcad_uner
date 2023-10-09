from typing import Any, Optional, Iterable
from ..list_node import ListNode

class LinkedList:
    """Implementación de una Lista utilizando representación por enlaces."""
    
    def __init__(self) -> None:
        """Crea una lista vacía"""
        self._header: ListNode = ListNode(None, None)
        self._size: int = 0

    def __len__(self) -> int:
        """Indica la cantidad de elementos de la estructura.

        Returns:
            int: entero que indica la cantidad actual de elementos almacenados en la lista. 
        """
        return self._size

    def __str__(self) -> str:
        """Concatena en un único string todos los elementos de la lista.

        Returns:
            str: string con todos los elementos que contiene la lista.
        """
        #Si la estructura está vacía => retorno siempre lo mismo.
        if self.is_empty():
            return "LinkedList()"
        
        res = "" # inicializo resultado con el string vacío

        actual = self._header.next # Inicio con el primer nodo de la estructura.

        while actual: # Si el elemento actual no es None
            # Lo proceso
            res += str(actual.element) + ", "
            # Continúo con el siguiente.
            actual = actual.next

        # Quito las dos últimas posiciones del string.
        res = res[:-2]

        return f"LinkedList({res})"

    def __contains__(self, item: Any) -> bool:
        """Indica si un elemento forma parte de la estructura.

        Args:
            item (Any): el elemento a buscar en la estructura.

        Returns:
            bool: Devuelve True en caso de encontrar el elemento, caso contrario False.
        """
        return self.index_of(item) >= 0 # Si index_of devuelve un valor mayor o igual que cero => encontré el valor que estaba buscando.

    def __getitem__(self, key: int) -> Optional[Any]:
        """Devuelve el elemento ubicado en la posición key de la lista.

        Args:
            key (int): índice a buscar en la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía o si el índice está fuera de rango.

        Returns:
            Any: Devuelve el valor almacenado por la posición indicada por key, caso contrario, None.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if abs(key) >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")
        
        # Si el índice es negativo, calculo el valor que le corresponde
        if key < 0:
            key = len(self) - abs(key)

        i = 0
        actual = self._header.next # Inicio en el primer nodo.
        while actual: # Si existe
            if i == key: # Si el valor de i coincide con el de key
                return actual.element #Devuelvo el valor del nodo en el que estoy ubicado.
            actual = actual.next # Caso contrario continúo con el siguiente nodo.
            i += 1

        return None
    
    def __setitem__(self, key: int, value: Any) -> None:
        """Establece como nuevo elemento value para la posición de lista indicada por key.

        Args:
            key (int): posición que se va a modificar.
            value (Any): nuevo elemento que va a ocupar la posición indicada por key.

        Raises:
            Exception: Arroja excepciones si la estructura está vacía o si el índice está fuera de rango.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if abs(key) >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")
        
        # Si el índice es negativo, calculo el valor que le corresponde
        if key < 0:
            key = len(self) - abs(key)

        i = 0 
        
        actual = self._header.next # Inicio en el primer nodo
        
        while actual: # Si el nodo existe...
            if i == key: # Verifico si el índice coincide con el pasado por parámetro
                actual.element = value
                return
            actual = actual.next
            i += 1

    def __delitem__(self, key: int) -> None:
        """Elimina de la estructura el valor ubicado en la posición indicada por key.

        Args:
            key (int): índice del elemento que se va a quitar de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía o si el índice está fuera de rango.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if abs(key) >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")
        
        # Si el índice es negativo, calculo el valor que le corresponde
        if key < 0:
            key = len(self) - abs(key)

        i = 0

        previo = None
        actual = self._header.next # Arranco en el primer nodo de la lista.
        while actual: # Si existe...
            if i == key: # Si el i es igual a key => corto.
                break
            previo = actual # Guardo el valor de actual en previo.
            actual = actual.next # Continúo con el siguiente nodo.
            i += 1

        # Si previo existe => elimino el nodo actual haciendo que el siguiente del previo sea igual al siguiente de actual
        if previo: 
            previo.next = actual.next # type: ignore
        else:
            # Si previo no existe => se está queriendo eliminar el primer nodo.
            self._header.next = actual.next # type: ignore

        self._size -= 1

    def __iter__(self) -> Iterable[Any]:
        """Crea un iterador sobre la lista.

        Yields:
            _type_: _description_
        """
        # Se ubica en el primer nodo.
        actual = self._header.next
        
        #Si existe un nodo
        while actual:
            #Devuelve el elemento del nodo actual
            yield actual.element
            
            #Continúa con el siguiente.
            actual = actual.next
            
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.
        
        Returns:
            bool: Devuelve True si la lista no tiene ningún elemento, caso contrario False.
        """
        return self._size == 0

    def append(self, elem: Any) -> None:
        """ Agrega un elemento al final de la estructura.

        Args:
            elem (Any): el elemento que va a quedar ubicado al final de la lista.
        """
        nuevo_nodo = ListNode(elem)
        # Si la lista está vacía => el nuevo nodo es el primero.
        if self.is_empty():
            self._header.next = nuevo_nodo
        else:
            # Caso contrario => me muevo hasta el final...
            actual = self._header

            while actual.next:
                actual = actual.next

            # Agrego el nuevo nodo como siguiente del último.
            actual.next = nuevo_nodo

        self._size += 1

    def index_of(self, elem: Any) -> int:
        """ Devuelve la ubicación elem en la estructura. 
        
        Args:
            elem (Any): El elemento a buscar.

        Returns:
            int: Devuelve la posición de elem en la estructura, en caso de no encontrarlo, -1.
        """
        i = 0

        actual = self._header.next # Me ubico en el primer nodo
        
        while actual:
            # Si el elemento de actual es el que estoy buscando devuelvo el valor de i.
            if actual.element == elem:
                return i
            
            actual = actual.next # Continúo con el siguiente nodo.
            i += 1

        return -1
