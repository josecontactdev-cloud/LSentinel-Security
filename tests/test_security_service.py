from services.security_service import SecurityService


def test_ssl_check_returns_expected_keys():
    result = SecurityService.ssl_check("google.com")

    assert "domain" in result
    assert "issuer" in result
    assert "subject" in result
    assert "expires" in result
