from typing import Any, Tuple
from .vertex import Vertex

class Edge:
    """ Representa la arista de un grafo. """
    __slots__ = '_origin', '_destination', '_element'
    
    def __init__(self, u: Vertex, v: Vertex, x: Any) -> None:
        self._origin = u
        self._destination = v
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
        return f"origin: {self._origin} - destination: {self._destination}, element: {self._element}"
        
    def __eq__(self) -> bool:
        return (self._origin, self._destination) == (self._origin, self._destination)
    
    def __hash__(self) -> int:
        return hash((self._origin, self._destination))
        
    def endpoints(self) -> Tuple[Vertex, Vertex]:
        """ Devuelve una tupla formada por los vértices 
        que conecta esta arista.

        Returns:
            Tuple[Vertex, Vertex]: Devuelve el vértice origen y destino 
            en ese orden como una tupla.
        """
        return (self._origin, self._destination)
    
    def opposite(self, v: Vertex) -> Vertex:
        """ Devuelve el vértice correspondiente al otro extremo de la arista.

        Args:
            v (Vertex): Si v es el vértice destino, devuelve el de origen.
            Caso contrario devuelve el de destino.

        Returns:
            Vertex: vértice al otro extremo de la arista.
        """
        return self._destination if v is self._origin else self._origin
    
    
    
    