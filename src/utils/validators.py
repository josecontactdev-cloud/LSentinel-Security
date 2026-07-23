import ipaddress
import re

from core.exceptions import ValidationError


class Validator:
    """Utility class for validating user input."""

    DOMAIN_REGEX = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)" r"(\.[A-Za-z]{2,})+$")

    @classmethod
    def validate_domain(cls, domain: str) -> str:
        domain = domain.strip().lower()

        if not cls.DOMAIN_REGEX.fullmatch(domain):
            raise ValidationError(f"Invalid domain: {domain}")

        return domain

    @classmethod
    def validate_ip(cls, ip: str) -> str:
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError as err:
            raise ValidationError(f"Invalid IP address: {ip}") from err

    @staticmethod
    def validate_hash_algorithm(algorithm: str) -> str:
        allowed = {
            "sha256",
            "sha512",
            "sha1",
            "md5",
            "blake2b",
        }

        algorithm = algorithm.lower()

        if algorithm not in allowed:
            raise ValidationError(f"Unsupported algorithm: {algorithm}")

        return algorithm
