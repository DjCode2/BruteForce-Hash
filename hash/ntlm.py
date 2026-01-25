from passlib.hash import nthash
from .hasher import Hasher

class NTLMHasher(Hasher):
    def hash(self, word: bytes) -> bytes:
        # nthash.hash() retourne une chaîne hexadécimale
        hex_hash = nthash.hash(word.decode())
        return bytes.fromhex(hex_hash)