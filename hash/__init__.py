from .ntlm import NTLMHasher
from .md5 import MD5Hasher
from .sha1 import SHA1Hasher
from .sha256 import SHA256Hasher

HASHERS = {
    "NTLM": NTLMHasher,
    "MD5": MD5Hasher,
    "SHA1" : SHA1Hasher,
    "SHA256" : SHA256Hasher,
}

__all__ = ["HASHERS"]