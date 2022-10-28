from typing import Any, List, Generator
from .hashmap_base import HashMapBase
from .unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """ Implementación de Tabla Hash Utilizando encadenamiento externo

    Args:
        HashMapBase: clase donde se define la interfaz pública de ChainHashMap.
    """
    
    def __init__(self, cap=11, p=109345121) -> None:
        """ Invoca al constructor de HashMapBase, define que 
        self._table es de tipo List que contiene buckets de tipo UnsortedTableMap y 
        la inicializa con elementos de tipo None.

        Args:
            cap (int, optional): _description_. Defaults to 11.
            p (int, optional): _description_. Defaults to 109345121.
        """
        super().__init__(cap, p)
        self._table : List[UnsortedTableMap | None] = [None] * cap
        
    def __str__(self) -> str:
        """ Convierte en str cada uno de los buckets y los concatena en un único str.

        Returns:
            str: Devuelve un str con todos los Ítems del Mapeo.
        """
        res = ",\n\t".join([str(bucket) for bucket in self.iter_items()])
        return f"ChainHashMap(\n\t{res})"
    
    def _bucket_getitem(self, j: int, k: Any) -> Any:
        """ Devuelve el ítem ubicado en la posición j que tiene clave k.

        Args:
            j (int): posición que resultó de la función hash sobre k.
            k (Any): clave de la entrada que se busca.

        Raises:
            KeyError: Arroja KeyError si el bucket indicado por j no tiene elementos.

        Returns:
            Any: devuelve el valor correspondiente a la clave k que está en el bucket de la posición j.
        """
        bucket = self._table[j]
        
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  
        
        return bucket[k]
    
    def _bucket_setitem(self, j : int , k : Any, v : Any):
        """ Inserta/actualiza con v como nuevo valor la entrada con clave k
        en el bucket j.

        Args:
            j (int): posición que resultó de la función hash sobre k.
            k (Any): clave de la entrada que corresponde insertar/actualizar.
            v (Any): nuevo valor de la entrada.
        """
        # Si el bucket está vacío entonces creo una nueva instancia de UnsortedTableMap en él.
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        
        # Determino la cantidad de elementos que tiene actualmente el mapeo en el bucket.
        oldsize = len(self._table[j])  # type: ignore
        
        #Inserto/actualizo el valor de la entrada con clave k 
        self._table[j][k] = v # type: ignore

        # Si la cantidad de claves en el bucket se incrementó actualizo self._n
        if len(self._table[j]) > oldsize: # type: ignore
            self._n += 1
    
    def _bucket_delitem(self, j : int, k : Any):
        """ Elimina del bucket en la posición j la entrada con clave k.

        Args:
            j (int): posición que resultó de la función hash sobre k.
            k (Any): clave de la entrada a eliminar.

        Raises:
            KeyError: arroja excepción si no hay entrada con clave k en el bucket j.
        """
        bucket = self._table[j]
        
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        
        # Elimina la clave k del bucket.
        del bucket[k]
        
    def __iter__(self) -> Generator[Any, None, None]:
        """ Devuelve un generator sobre self._table 

        Yields:
            Generator[Any, None, None]: devuelve todas las claves del Mapeo.
        """
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
                    
    def iter_items(self) -> Generator[UnsortedTableMap, None, None]:
        """ Devuelve un generator sobre el Mapeo que devuelve todos los ítems.

        Yields:
            Generator[UnsortedTableMap, None, None]: devuelve los mapeos de toda la tabla.
        """
        for bucket in self._table:
            if bucket is not None:
                yield bucket
                    