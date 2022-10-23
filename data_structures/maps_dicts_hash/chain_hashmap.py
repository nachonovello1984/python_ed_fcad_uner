from typing import Any, List, Union, Optional
from .hashmap_base import HashMapBase
from .unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    
    def __init__(self, cap=11, p=109345121) -> None:
        super().__init__()
        self._table : List[UnsortedTableMap | None] = [None] * cap
        
    def __str__(self) -> str:
        
        res = ",\n\t".join([str(bucket) for bucket in self.iter_items()])
        return f"ChainHashMap(\n\t{res})"
    
    def _bucket_getitem(self, j: int, k: Any) -> Any:
        bucket = self._table[j]
        
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  
        
        return bucket[k]
    
    def _bucket_setitem(self, j : int , k : Any, v : Any):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
            
        oldsize = len(self._table[j])  # type: ignore
        self._table[j][k] = v # type: ignore
        if len(self._table[j]) > oldsize: # type: ignore
            self._n += 1
    
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        
        del bucket[k]
        
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
                    
    def iter_items(self):
        for bucket in self._table:
            if bucket is not None:
                yield bucket
                    