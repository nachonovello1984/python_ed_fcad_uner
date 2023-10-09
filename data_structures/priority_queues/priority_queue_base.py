from typing import Any

class PriorityQueueBase:
    """Clase base para la implementación de Colas de Prioridad. Define la clase _Item."""
    class _Item:
        
        """Clase para almacenar items de Cola de Prioridad."""
        __slots__ = '_key', '_value'
        
        def __init__(self, k: Any, v: Any) -> None:
            self._key = k
            self._value = v
        
        def __lt__(self, other: Any) -> bool:
            """Compara los items por su propiedad key.

            Args:
                other (Any): objeto con el que hacer la comparación.

            Returns:
                bool: Devuelve verdadero si el objeto que recibe el mensaje es menor que el pasado por parámetro.
            """
            return self._key < other._key
        
        def __eq__(self, other: Any) -> bool:
            """Compara los items por su propiedad key.

            Args:
                other (Any): objeto con el que hacer la comparación.

            Returns:
                bool: Devuelve verdadero si el objeto que recibe el mensaje es igual que el pasado por parámetro.
            """
            return self._key == other._key
        
        def __repr__(self) -> str:
            """Convierte en str las propiedades del _Item.

            Returns:
                str: concatena en un único string todas las propiedades del _Item.
            """
            return f"_Item(key={self._key}, value={self._value})"
            
        def __str__(self) -> str:
            """Ídem __repr__()

            Returns:
                str: Ídem __repr__()
            """
            return repr(self)