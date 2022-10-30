from typing import Any

class Vertex:
    """ Representa el vértice de un grafo. """
    __slots__ = '_element'
    
    def __init__(self, x: Any) -> None:
        self._element = x
        
    @property
    def element(self) -> Any:
        return self._element
    
    @element.setter
    def element(self, value: Any) -> None:
        self._element = value
        
    def __repr__(self) -> str:
        return str(self)
        
    def __str__(self) -> str:
        return str(self._element)
    
    def __eq__(self, other: 'Vertex') -> bool:
        return id(self) == id(other)
            
    def __hash__(self) -> int:
        return hash( id(self) )