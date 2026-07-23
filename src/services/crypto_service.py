import hashlib


class CryptoService:
    """Service responsible for cryptographic operations."""

    _ALGORITHMS = {
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
        "sha1": hashlib.sha1,
        "md5": hashlib.md5,
        "blake2b": hashlib.blake2b,
    }

    @classmethod
    def hash_text(cls, text: str, algorithm: str = "sha256") -> str:
        algorithm = algorithm.lower()

        if algorithm not in cls._ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        return cls._ALGORITHMS[algorithm](text.encode("utf-8")).hexdigest()