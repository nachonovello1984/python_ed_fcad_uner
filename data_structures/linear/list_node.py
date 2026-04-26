from typing import Optional

class ListNode[T]:
    
    __slots__ = "element", "next"
    
    def __init__(self, element : T, next : Optional['ListNode'] = None) -> None:
        self.element = element
        self.next : Optional['ListNode'] = next