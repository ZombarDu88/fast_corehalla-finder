# libs/colored_terminal/__init__.py

import os
os.system('color')

#cmd background text
class Colors:
    def __init__(self):

        self.BLACK = '\033[30m'
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m' # orange on some systems
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'
        self.CYAN = '\033[36m'
        self.LIGHT_GRAY = '\033[37m'
        self.DARK_GRAY = '\033[90m'
        self.BRIGHT_RED = '\033[91m'
        self.BRIGHT_GREEN = '\033[92m'
        self.BRIGHT_YELLOW = '\033[93m'
        self.BRIGHT_BLUE = '\033[94m'
        self.BRIGHT_MAGENTA = '\033[95m'
        self.BRIGHT_CYAN = '\033[96m'
        self.WHITE = '\033[97m'

        self.RESET = '\033[0m' # called to return to standard terminal text color

        #cmd background
        self.BACKGROUND_BLACK = '\033[40m'
        self.BACKGROUND_RED = '\033[41m'
        self.BACKGROUND_GREEN = '\033[42m'
        self.BACKGROUND_YELLOW = '\033[43m' # orange on some systems
        self.BACKGROUND_BLUE = '\033[44m'
        self.BACKGROUND_MAGENTA = '\033[45m'
        self.BACKGROUND_CYAN = '\033[46m'
        self.BACKGROUND_LIGHT_GRAY = '\third-party033[47m'
        self.BACKGROUND_DARK_GRAY = '\033[100m'
        self.BACKGROUND_BRIGHT_RED = '\033[101m'
        self.BACKGROUND_BRIGHT_GREEN = '\033[102m'
        self.BACKGROUND_BRIGHT_YELLOW = '\033[103m'
        self.BACKGROUND_BRIGHT_BLUE = '\033[104m'
        self.BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
        self.BACKGROUND_BRIGHT_CYAN = '\033[106m'
        self.BACKGROUND_WHITE = '\033[107m'