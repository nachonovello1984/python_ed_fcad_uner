from typing import Any, Tuple
from .vertex import Vertex

class Edge:
    __slots__ = '_origin', '_destination', '_element'
    
    def __init__(self, u: Vertex, v: Vertex, x: Any) -> None:
        self._origin = u
        self._destination = v
        self._element = x
        
    def __repr__(self) -> str:
        return str(self)
        
    def __str__(self) -> str:
        return f"destination: {self._destination}, element: {self._element}"
        
    def __eq__(self) -> bool:
        return (self._origin, self._destination) == (self._origin, self._destination)
    
    def __hash__(self) -> int:
        return hash((self._origin, self._destination))
        
    def endpoints(self) -> Tuple[Vertex, Vertex]:
        return (self._origin, self._destination)
    
    def opposite(self, v: Vertex) -> Vertex :
        return self._destination if v is self._origin else self._origin
    
    def element(self) -> Any:
        return self._element
    
    