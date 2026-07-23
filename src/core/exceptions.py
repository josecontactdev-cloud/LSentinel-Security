class LSentinelError(Exception):
    """Base exception for all LSentinel errors."""


class ConfigurationError(LSentinelError):
    """Raised when the application configuration is invalid."""


class HashAlgorithmError(LSentinelError):
    """Raised when an unsupported hash algorithm is requested."""


class NetworkError(LSentinelError):
    """Raised when a network operation fails."""


class WhoisLookupError(LSentinelError):
    """Raised when a WHOIS lookup fails."""


class SSLCheckError(LSentinelError):
    """Raised when an SSL certificate check fails."""


class ValidationError(LSentinelError):
    """Raised when user input validation fails."""