from typing import Any, Union

class ListNode:
    
    __slots__ = "element", "next"
    
    def __init__(self, element : Any, next = None) -> None:
        self.element = element
        self.next : Union[ListNode, None] = next