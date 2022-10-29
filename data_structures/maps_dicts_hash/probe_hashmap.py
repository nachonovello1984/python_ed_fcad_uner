from typing import Any, Tuple, Generator
from .hashmap_base import HashMapBase

class ProbeHashMap(HashMapBase):
    """ Implementa una Tabla Hash que utiliza direccionamiento abierto como
    técnica de resolución de colisiones a través de la Prueba Lineal.

    Args:
        HashMapBase: Esta clase configura la interfaz pública de ProbeHashMap.
    """
    _AVAIL = object()
    
    def __str__(self) -> str:
        """ Devuelve un str con todas las entradas en la tabla.

        Returns:
            str: concatena en un str todas las entradas y el índice que ocupan en la tabla.
        """
        res = ",\n\t".join([f"i: {i}, item: {item}" for i, item in enumerate(self._table) if not self._is_available(i)])
        
        return f"ProbeHashMap({res})"

    def _is_available(self, j: int) -> bool:
        """  Indica si la posición j está disponible.

        Args:
            j (int): posición a controlar si está disponible.

        Returns:
            bool: True si la posición es None o tiene un objeto AVAIL.
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j: int, k: Any) -> Tuple[bool, int]:
        """ Busca una posición a través de prueba lineal de una clave k cuya función hash retornó j.
        Indica si la posición está ocupada o no y cual es la posición disponible.

        Args:
            j (int): inicia como la posición calculada por la función hash. El parámetro también se utiliza para guardar el resultado de las distintas iteraciones de la prueba lineal.
            k (Any): clave que se está buscando.

        Returns:
            Tuple[bool, int]: el primer valor indica si la posición está disponible y el segundo cuál es el subíndice disponible.
        """
        first_available = None
        while True:
            # Si la posición está disponible
            if self._is_available(j):
                # Si first_available es None
                if first_available is None:
                    first_available = j  # El valor de first_available es j y continúa
                
                # Si la posición j no está ocupada    
                if self._table[j] is None:
                    return (False, first_available)  # fallo en la búsqueda.
            
            # Si existe un elemento con clave k en j...
            elif k == self._table[j]._key: # type: ignore
                return (True, j)  # se encontró una coincidencia.
            j = (j + 1) % len(self._table)  # continúa buscando (de manera cíclica)

    def _bucket_getitem(self, j : int, k : Any) -> Any:
        """ Devuelve el valor asociado a la clave k en la posición j

        Args:
            j (int): posición donde se comienza a buscar la entrada para k
            k (Any): clave cuyo valor se busca.

        Raises:
            KeyError: arroja error si no se encuentra una entrada con clave k en la tabla.

        Returns:
            Any: retorna el valor asociado a la clave k.
        """
        # Utiliza self._find_slot para determinar si la posición está ocupada o no.
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no se encontraron coincidencias.
        
        return self._table[s]._value # type: ignore

    def _bucket_setitem(self, j: int, k : Any, v : Any) -> None:
        """ Inserta/actualiza el valor asociado para la entrada con clave k.

        Args:
            j (int): posición resultando de la función hash sobre k.
            k (Any): clave cuya entrada se quiere insertar/actualizar.
            v (Any): valor a insertar/actualizar.
        """
        # Busca la k en la tabla.
        found, s = self._find_slot(j, k)
        # Si no lo encontró lo actualiza
        if not found:
            self._table[s] = self._Item(k,v) # 
            self._n += 1 # incrementa el tamaño en 1
        else:
            self._table[s]._value = v # type: ignore . Sobreescribe el valor existente.

    def _bucket_delitem(self, j: int, k: Any) -> None:
        """ Elimina la entrada con clave k y posición j.

        Args:
            j (int): posición resultando de la función hash sobre k.
            k (Any): clave cuya entrada se quiere eliminar.

        Raises:
            KeyError: arroja excepción cuando no se encuentra una posición para k en la tabla.
        """
        found, s = self._find_slot(j, k)  # type: ignore
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no se encontraron coincidencias.
        
        self._table[s] = ProbeHashMap._AVAIL # marca como disponible la posición indicada por s

    def __iter__(self) -> Generator[Any, None, None]:
        """ Devuelve un generator sobre self._table.

        Yields:
            Generator[Any, None, None]: devuelve todas las claves del Mapeo.
        """
        for j in range(len(self._table)): # accede a todos los elementos de la tabla.
            if not self._is_available(j):
                yield self._table[j]._key # type: ignore