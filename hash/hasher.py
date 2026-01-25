from abc import ABC, abstractmethod

#classe abstraite générale
class Hasher(ABC):
    @abstractmethod
    def hash(self, word: bytes) -> bytes:
        pass


