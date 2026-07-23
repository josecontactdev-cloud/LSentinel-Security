import aiohttp
import dns.resolver


class NetworkService:
    """Handles network related operations."""

    @staticmethod
    async def ip_lookup(ip: str) -> dict:
        url = f"https://ipwho.is/{ip}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    @staticmethod
    def dns_lookup(domain: str) -> dict:
        records = ["A", "AAAA", "MX", "TXT", "NS"]

        result = {}

        for record in records:
            try:
                answers = dns.resolver.resolve(domain, record)

                result[record] = [str(answer) for answer in answers]

            except Exception:
                result[record] = []

        return result
