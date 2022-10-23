from abc import ABC, abstractmethod
from collections.abc import MutableMapping

class MapBase(MutableMapping, ABC):
    
    class _Item:
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
            
        def __str__(self):
            return f"({self._key}, {self._value})"
            
        def __eq__(self, other):
            return self._key == other._key
        
        def __ne__(self, other):
            return not (self == other)
        
        def __lt_(self, other):
            return self._key < other._key