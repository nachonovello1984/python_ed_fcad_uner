from abc import ABC, abstractmethod
from typing import Any, List, Optional
from random import randrange
from .map_base import MapBase

class HashMapBase(MapBase, ABC):
    """ Clase abstracta que configura la interfaz de tabla hash.

    Args:
        MapBase: _description_
        ABC: _description_
    """
    
    def __init__(self, cap=11, p=109345121) -> None:
        """_summary_

        Args:
            cap (int, optional): _description_. Defaults to 11.
            p (int, optional): _description_. Defaults to 109345121.
        """
        self._table : List[Optional[Any]] = cap * [None]
        self._n = 0 # número de entradas en el mapeo.
        self._prime = p # número primo para compresión MAD
        self._scale = 1 + randrange(p - 1) # escala de 1 a p - 1 para MAD
        self._shift = randrange(p) # variación de 0 a p - 1 para MAD
        
    @abstractmethod
    def _bucket_getitem(self, j : int , k : Any) -> Any:
        """ Método abstracto que define cómo se encuentra 
        un valor en la posición j y con clave k.

        Args:
            j (int): índice que resultó de aplicar función hash.
            k (Any): clave del ítem a obtener

        Returns:
            Any: valor asociada con la clave k en el bucket indicado por j.
        """
        pass
    
    @abstractmethod
    def _bucket_setitem(self, j : int, k : Any, v : Any) -> None:
        """ Método abstracto que define cómo se inserta/modifica 
        una entrada en la posición j y con clave k.

        Args:
            j (int): índice que resultó de la función hash sobre k.
            k (Any): clave de la entrada a insertar/actualizar.
            v (Any): valor para establecer como asociado a k en j.
        """
        pass
    
    @abstractmethod
    def _bucket_delitem(self, j : int, k : Any) -> None:
        """ Método abstracto que define cómo se elimina
        una entrada en la posición j y con clave k.

        Args:
            j (int): índice que resultó de aplicar la función hash a k.
            k (Any): clave de la entrada que se va a eliminar.
        """
        pass
        
    def _hash_function(self, k : Any) -> int:
        """Aplica la función hash sobre la clave k y luego función de compresión MAD.

        Args:
            k (Any): clave sobre la que se calcula la posición dentro del espacio de tabla.

        Returns:
            int: índice dentro del espacio definido por self._table
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self) -> int:
        """ Devuelve la cantidad de claves diferentes que hay en el mapeo.

        Returns:
            int: cantidad de claves diferentes en el mapeo.
        """
        return self._n
    
    def __getitem__(self, k : Any) -> Any:
        """ Devuelve el valor asociado a la clave k.

        Args:
            k (Any): clave para la que se busca el valor asociado.

        Returns:
            Any: devuelve el valor asociado a la clave k.
        """
        # Calcula el índice a través de la función hash.
        j = self._hash_function(k)
        
        # Intenta obtener el valor asociado a k en j.
        return self._bucket_getitem(j, k)
    
    def __setitem__(self, k : Any, v : Any) -> None:
        """ Inserta/Modifica en el Mapeo la entrada con valor v y clave k.

        Args:
            k (Any): clave que se quiere insertar/modificar. 
            v (Any): valor que se quiere insertar/modificar
        """
        # Calcula el índice a través de la función hash.
        j = self._hash_function(k)

        # Inserta/actualiza la entrada con clave k y valor v.        
        # La subclase se encarga de actualizar el valor self._n
        self._bucket_setitem(j, k, v) 
        
        # Mantener el factor de carga <= 0.5
        if self._n > len(self._table) // 2: 
            # Redimensiona la tabla.
            self._resize(2 * len(self._table) - 1)
            
    def __delitem__(self, k : Any) -> None:
        """ Elimina la entrada con clave k del mapeo.

        Args:
            k (Any): clave cuya entrada se quiere eliminar del mapeo.
        """
        # Calcula el índice a través de la función hash.
        j = self._hash_function(k)
        
        # Elimina la entrada con clave k en j.
        self._bucket_delitem(j, k)
        
    def _resize(self, c : int) -> None:
        """ Redimensiona la tabla según la capacidad indicada por c.

        Args:
            c (int): nueva longitud de self._table.
        """
        # Uso items para obtener todos los elementos y dejarlos en una lista Python.
        old = list(self.items()) 
        
        # Reinicio la tabla a la capacidad especificada.
        self._table : List[Any | None]= c * [None] 
        
        #Reinicio el valor de v a 0.
        self._n = 0
        
        for (k, v) in old:
            # Con cada asignación se invoca a self.__setitem__ y se actualiza self._n
            self[k] = v 
        
