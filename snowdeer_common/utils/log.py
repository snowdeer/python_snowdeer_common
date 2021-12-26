import threading
from datetime import datetime


class Log:
    __BLACK = "\033[30m"
    __RED = "\033[31m"
    __GREEN = "\033[32m"
    __YELLOW = "\033[33m"
    __BLUE = "\033[34m"
    __MAGENTA = "\033[35m"
    __CYAN = "\033[36m"
    __WHITE = "\033[37m"
    __UNDERLINE = "\033[4m"
    __RESET = "\033[0m"

    __lock = threading.Lock()

    @classmethod
    def d(cls, message):
        Log.__print_log(Log.__GREEN, message)

    @classmethod
    def i(cls, message):
        Log.__print_log(Log.__YELLOW, message)

    @classmethod
    def w(cls, message):
        Log.__print_log(Log.__MAGENTA, message)

    @classmethod
    def e(cls, message):
        Log.__print_log(Log.__RED, message)

    @classmethod
    def __print_log(cls, color: int, message: str):
        with Log.__lock:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            print(f"{color}[{timestamp}] {message}{Log.__RESET}")
