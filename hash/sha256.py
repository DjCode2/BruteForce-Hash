import hashlib
from .hasher import Hasher

class SHA256Hasher(Hasher):
    def hash(self, word: bytes) -> bytes:
        return hashlib.sha256(word).digest()
