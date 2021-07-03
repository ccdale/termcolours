import sys

__version__ = "0.1.4"


class termcolours:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"

    HEADER = "\033[35m"
    OKBLUE = "\033[34m"
    OKGREEN = "\033[32m"
    OK = "\033[32m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"

    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __init__(self):
        try:
            self.hangingline = False
            self.colours = {
                RED: "\033[31m",
                red: "\033[31m",
                GREEN: "\033[32m",
                green: "\033[32m",
                YELLOW: "\033[33m",
                yellow: "\033[33m",
                BLUE: "\033[34m",
                blue: "\033[34m",
                MAGENTA: "\033[35m",
                magenta: "\033[35m",
            }
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def colourtext(msg, colour=None, background=None):
        if colour is not None:
            xcol = colour.upper()

    def tcfail(self):
        try:
            return f"{self.FAIL}[FAIL]{self.ENDC}"
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def mopf(self):
        try:
            print(self.tcfail())
            self.hangingline = False
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def tcdone(self):
        try:
            return f"{self.OKGREEN}[DONE]{self.ENDC}"
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def mopd(self):
        try:
            print(self.tcdone())
            self.hangingline = False
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def tcp(self, msg):
        try:
            return f"{msg:<74}"
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def mop(self, msg):
        try:
            print(self.tcp(msg), end="", flush=True)
            self.hangingline = True
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise

    def mopp(self, msg):
        try:
            if self.hangingline:
                print()
                self.hangingline = False
            print(msg)
        except Exception as e:
            exci = sys.exc_info()[2]
            lineno = exci.tb_lineno
            fname = exci.tb_frame.f_code.co_name
            ename = type(e).__name__
            msg = f"{ename} Exception at line {lineno} in function {fname}: {e}"
            log.error(msg)
            raise
