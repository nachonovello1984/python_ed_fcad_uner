from abc import ABC, abstractmethod
from typing import Any, List
from random import randrange
from .map_base import MapBase

class HashMapBase(MapBase, ABC):
    
    def __init__(self, cap=11, p=109345121) -> None:
        self._table : List[Any | None] = cap * [None]
        self._n = 0 # número de entradas en el mapeo.
        self._prime = p # número primo para compresión MAD
        self._scale = 1 + randrange(p - 1) # escala de 1 a p - 1 para MAD
        self._shift = randrange(p) # variación de 0 a p - 1 para MAD
        
    @abstractmethod
    def _bucket_getitem(self, j : int , k : Any) -> Any:
        pass
    
    @abstractmethod
    def _bucket_setitem(self, j : int, k : Any, v : Any) -> None:
        pass
    
    @abstractmethod
    def _bucket_delitem(self, j : int, k : Any) -> None:
        pass
        
    def _hash_function(self, k : Any) -> int:
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self) -> int:
        return self._n
    
    def __getitem__(self, k : Any) -> Any:
        j = self._hash_function(k)
        
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k : Any, v : Any) -> None:
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v) # la implementación mantiene actualizado el valor de self._n
        if self._n > len(self._table) // 2: # Mantener el factor de carga <= 0.5
            self._resize(2 * len(self._table) - 1)
            
    def __delitem__(self, k : Any) -> None:
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        
    def _resize(self, c : int) -> None:
        old = list(self.items()) # uso items para obtener todos los elementos.
        self._table : List[Any | None]= c * [None] # reinicia la tabla a la capacidad especificada.
        self._n = 0
        for (k, v) in old:
            self[k] = v # con cada asignación se invoca a self.__setitem__ y se actualiza self._n
        