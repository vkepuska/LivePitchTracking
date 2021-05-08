import tkinter as tk                                # GUI toolkit
from gui.commandForm import CommandForm             # controls for PDA widget
from plots.pdaPlots import PdaPlots                 # sound plots widget
from gui.elapsedTime import ElapsedTime             # processing time widget


class SEA(object):
    """Set up and manage the graphical interface."""

    # Constants
    TITLE = 'Speech Emotion Analyzer'               # window title
    WINDOW_WIDTH = 480                              # pixels across
    WINDOW_HEIGHT = 800                             # pixels up/down

    def __init__(self):
        """Construct object."""
        self.__win = tk.Tk()                        # GUI object
        self.__configure()                          # initialize the look
        self.__command = CommandForm(self.__win)    # command form object
        self.__plots = PdaPlots(self.__win)         # auditory plots object
        self.__elapsed = ElapsedTime(self.__win)    # elapsed time object
        self.__command.plots = self.__plots         # provide plots to command
        self.__plots.elapsed = self.__elapsed       # elps-time->plot
        self.__plots.update()                       # start diplaying plots

    def run(self):
        """Activate the GUI."""
        self.__win.mainloop()

    @property
    def width(self):
        """Returns width of GUI window."""
        return self.__windowWidth

    @property
    def height(self):
        """Returns width of GUI window."""
        return self.__windowHeight

    def __configure(self):
        """Initialize the look of the GUI."""
        self.__win.geometry(self.__size())          # set window size
        self.__win.resizable()                      # allow user to resize
        self.__win.title(self.TITLE)                # title of window

    def __size(self):
        """Return window geometry relative to screen size."""
        # get screen size
        screenWidth = self.__win.winfo_screenwidth()    # get screen width
        screenHeight = self.__win.winfo_screenheight()  # get screen height

        # set window size to be within screen
        if screenWidth > screenHeight:
            # set window size to be within screen
            self.__windowWidth = self.WINDOW_WIDTH      # win width
            self.__windowHeight = self.WINDOW_HEIGHT    # win height
        else:
            # for mobile device, take over entire screen
            self.__windowWidth = screenWidth            # win width
            self.__windowHeight = screenHeight          # win height

        # format to string that for geometry call
        return "{}x{}".format(self.__windowWidth, self.__windowHeight)
