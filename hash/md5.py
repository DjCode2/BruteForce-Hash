import hashlib
from .hasher import Hasher

class MD5Hasher(Hasher):
    def hash(self, word: bytes) -> bytes:
        return hashlib.md5(word).digest()