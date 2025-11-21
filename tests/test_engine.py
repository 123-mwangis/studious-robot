from ai.engine import Assistant


def test_greeting():
    a = Assistant(use_openai=False)
    r = a.respond("hello")
    assert "hello" in r.lower()


def test_empty():
    a = Assistant(use_openai=False)
    r = a.respond("")
    assert "please say" in r.lower()


def test_exit():
    a = Assistant(use_openai=False)
    r = a.respond("exit")
    assert "goodbye" in r.lower()


def test_time():
    a = Assistant(use_openai=False)
    r = a.respond("what time is it?")
    assert "current time" in r.lower() or "i heard you" in r.lower()
from ai.engine import Assistant


def test_greeting():
    a = Assistant()
    resp = a.respond("Hello")
    assert "hello" in resp.lower()


def test_empty():
    a = Assistant()
    resp = a.respond("")
    assert "please" in resp.lower()
