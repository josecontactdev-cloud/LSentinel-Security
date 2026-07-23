import hashlib

from services.crypto_service import CryptoService


def test_sha256_hash():
    expected = hashlib.sha256("LSentinel".encode("utf-8")).hexdigest()

    result = CryptoService.hash_text("LSentinel", "sha256")

    assert result == expected
