import tkinter as tk                                # GUI toolkit
from universal.constants import DEFAULT_WINDOW_WIDTH
from universal.constants import WINDOW_WIDTH
from universal.constants import DEFAULT_WINDOW_HEIGHT
from universal.constants import WINDOW_HEIGHT
from gui.commandForm import CommandForm             # controls for PDA widget
from plots.pdaPlots import PdaPlots                 # sound plots widget
from gui.emotionForm import EmotionForm             # display emotions
from gui.elapsedTime import ElapsedTime             # processing time widget


class SEA(object):
    """Set up and manage the graphical interface."""

    # Constants
    TITLE = 'Speech Emotion Analyzer'               # window title
    COLOR = 'dim gray'                              # dark theme

    def __init__(self):
        """Construct object."""
        self.__win = tk.Tk()                        # GUI object
        self.__configure()                          # initialize the look
        self.__command = CommandForm(self.__win)    # command form object
        self.__plots = PdaPlots(self.__win)         # auditory plots object
        self.__emotions = EmotionForm(self.__win)   # emotion form object
        self.__elapsed = ElapsedTime(self.__win)    # elapsed time object
        self.__command.plots = self.__plots         # provide plots to command
        self.__plots.elapsed = self.__elapsed       # elps-time->plot

    def run(self):
        """Activate the GUI."""
        self.__win.mainloop()

    def __configure(self):
        """Initialize the look of the GUI."""
        self.__win.geometry(self.__size())          # set window size
        self.__win.title(self.TITLE)                # title of window
        self.__win.configure(background=self.COLOR) # background color

    def __size(self):
        """Return window geometry relative to screen size."""
        # get screen size
        screenWidth = self.__win.winfo_screenwidth()    # get screen width
        screenHeight = self.__win.winfo_screenheight()  # get screen height

        # set window size to be within screen
        if screenWidth < screenHeight:
            # for portrait mode, take over entire screen
            WINDOW_WIDTH = screenWidth            # win width
            WINDOW_HEIGHT = screenHeight          # win height
        else:
            WINDOW_WIDTH = DEFAULT_WINDOW_WIDTH            # win width
            WINDOW_HEIGHT = DEFAULT_WINDOW_HEIGHT          # win height

        # format to string that for geometry call
        return "{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT)
