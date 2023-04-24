from typing import Any, Optional

class ListNode:
    
    __slots__ = "element", "next"
    
    def __init__(self, element : Any, next : Optional['ListNode'] = None) -> None:
        self.element = element
        self.next : Optional['ListNode'] = next