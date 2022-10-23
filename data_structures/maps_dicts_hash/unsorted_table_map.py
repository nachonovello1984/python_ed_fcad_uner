from .map_base import MapBase

class UnsortedTableMap(MapBase):
    
    def __init__(self):
        self._table  = []
        
    def __len__(self):
        return len(self._table)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        res = ", ".join([str(x) for x in self.iter_items()])
        return f"UnsortedTableMap({res})"
        
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))
    
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))
        
    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))
    
    def __iter__(self):
        for item in self._table:
            yield item._key
                
    def iter_items(self):
        for item in self._table:
            yield item