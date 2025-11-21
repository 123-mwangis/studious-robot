from ai.engine import Assistant


def test_greeting():
    a = Assistant()
    resp = a.respond("Hello")
    assert "hello" in resp.lower()


def test_empty():
    a = Assistant()
    resp = a.respond("")
    assert "please" in resp.lower()
