from termcolours import __version__
from termcolours import termcolours


def test_version():
    assert __version__ == "0.1.4"


def test_tcfail():
    tc = termcolours()
    xstr = tc.tcfail()
    assert xstr == "\033[31m[FAIL]\033[0m"


def test_tcdone():
    tc = termcolours()
    xstr = tc.tcdone()
    assert xstr == "\033[32m[DONE]\033[0m"


def test_tcp():
    tc = termcolours()
    msg = "A Test Message"
    xmsg = tc.tcp(msg)
    assert len(xmsg) == 74


def test_mopf(capfd):
    tc = termcolours()
    tc.mopf()
    captured = capfd.readouterr()
    assert captured.out == "\033[31m[FAIL]\033[0m\n"


def test_mopd(capfd):
    tc = termcolours()
    tc.mopd()
    captured = capfd.readouterr()
    assert captured.out == "\033[32m[DONE]\033[0m\n"


def test_mop(capfd):
    msg = "A test message"
    tc = termcolours()
    xmsg = tc.tcp(msg)
    tc.mop(msg)
    captured = capfd.readouterr()
    print(f"msg:|{xmsg}|")
    print(f"cap:|{captured.out}|")
    assert captured.out == f"{msg:<74}"
    assert (
        captured.out
        == "A test message                                                            "
    )


def test_split_msg(capfd):
    msg = "a test message"
    tc = termcolours()
    tc.mop(msg)
    tc.mopd()
    captured = capfd.readouterr()
    assert captured.out == f"{msg:<74}\033[32m[DONE]\033[0m\n"
