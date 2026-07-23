import socket
import ssl
from datetime import datetime

from core.exceptions import SSLCheckError


class SecurityService:
    """Handles SSL certificate operations."""

    @staticmethod
    def ssl_check(domain: str) -> dict:
        try:
            context = ssl.create_default_context()

            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(
                    sock,
                    server_hostname=domain
                ) as ssock:
                    cert = ssock.getpeercert()

            issuer = dict(x[0] for x in cert["issuer"])
            subject = dict(x[0] for x in cert["subject"])

            expires = datetime.strptime(
                cert["notAfter"],
                "%b %d %H:%M:%S %Y %Z"
            )

            return {
                "domain": domain,
                "issuer": issuer.get("organizationName", "Unknown"),
                "subject": subject.get("commonName", "Unknown"),
                "expires": expires,
            }

        except Exception as error:
            raise SSLCheckError(str(error))