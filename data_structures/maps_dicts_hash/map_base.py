from abc import ABC
from typing import Any
from collections.abc import MutableMapping

class MapBase(MutableMapping, ABC):
    """ Clase abstracta genérica que define la clase anidada _Item

    Args:
        MutableMapping: Hereda los métodos abstractos y concretos que definen la interfaz pública.
        ABC: para marcar MapBase como abstracta
    """
    
    class _Item:
        """ Define una asociación clave - valor """
        
        __slots__ = '_key', '_value'
        
        def __init__(self, k: Any, v: Any) -> None:
            self._key = k
            self._value = v
            
        def __str__(self) -> str:
            """Convierte en str el par _key, _value.

            Returns:
                str: convierte en str la entrada _key, _value.
            """
            return f"({self._key}, {self._value})"
            
        def __eq__(self, other) -> bool: #type: ignore
            """ Dos _Item son iguales si tienen la misma clave.

            Args:
                other (_Item): Se espera que other sea de tipo _Item.

            Returns:
                bool: True si las claves son iguales. False en caso contrario.
            """                
            return self._key == other._key
        
        def __ne__(self, other) -> bool:
            return not (self == other)
        
        def __lt__(self, other) -> bool: #type: ignore
            """Método utilizado para ordenar las claves en implementaciones de Mapeos ordenados.

            Args:
                other (_Item): instancia con la que comparar.

            Returns:
                bool: True si el objeto que recibe la llamada es menor que el pasado por parámetro.
            """
            return self._key < other._key