from termcolours import __version__
from termcolours import termcolours


def test_version():
    assert __version__ == "0.1.3"


def test_tcfail():
    tc = termcolours()
    xstr = tc.tcfail()
    assert xstr == "\033[31m[FAIL]\033[0m"
