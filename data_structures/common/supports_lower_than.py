from typing import Protocol

class SupportsLowerThan[K](Protocol):
    def __lt__(self, other: K) -> bool: ...
