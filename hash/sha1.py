import hashlib
from .hasher import Hasher

class SHA1Hasher(Hasher):
    def hash(self, word: bytes) -> bytes:
        return hashlib.sha1(word).digest()
