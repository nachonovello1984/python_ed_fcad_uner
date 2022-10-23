from typing import Any
from .hashmap_base import HashMapBase

class ProbeHashMap(HashMapBase):

    _AVAIL = object()

    def _is_available(self, j: int) -> bool:
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        first_available = None
        while True:
            if self._is_available(j):
                if first_available is None:
                    first_available = j  # marcar como primer posición disponible.
                if self._table[j] is None:
                    return (False, first_available)  # fallo en la búsqueda.
                elif k == self._table[j]._key:
                    return (True, j)  # se encontró una coincidencia.
            j = (j + 1) % len(self._table)  # continúa buscando (de manera cíclica)

    def _bucket_getitem(self, j : int, k : Any) -> Any:
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no se encontraron coincidencias.
        return self._table[s]._value

    def _bucket_setitem(self, j: int, k : Any, v : Any) -> None:
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v) # omerta
            self._n += 1 # incrementa el tamaño en 1
        else:
            self._table[s]._value = v # sobreescribe el valor existente.

    def _bucket_delitem(self, j: int, k: Any):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no se encontraron coincidencias.
        self._table[s] = ProbeHashMap._AVAIL # marca como disponible la posición indicada por s

    def __iter__(self):
        for j in range(len(self._table)): # accede a todos los elementos de la tabla.
            if not self._is_available(j):
                yield self._table[j]._key