from typing import Any, Union

class ListNode:
    
    __slots__ = "_element", "_next"
    
    def __init__(self, element : Any, next = None) -> None:
        self._element = element
        self._next : Union[ListNode, None] = next