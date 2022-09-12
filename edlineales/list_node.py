from typing import Any

class ListNode:
    
    __slots__ = "_element", "_next"
    
    def __init__(self, element : Any, next = None) -> None:
        self._element = element
        self._next = next