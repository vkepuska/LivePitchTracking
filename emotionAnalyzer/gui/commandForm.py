import tkinter as tk                                # GUI toolkit
from gui.micButton import MicButton                 # button to start microphone
from gui.fileButton import FileButton               # button to select file


class CommandForm(object):
    """Manages the window form for controlling the GUI."""

    COLOR = 'gray'                                  # background color
    RELATIVE_WIDTH = 1.0                            # entire width
    RELATIVE_HEIGHT = 0.1                           # top 0.1 of window

    def __init__(self, win):
        """Construct object."""
        # win   window application

        self.__frame = tk.Frame(win)                # create frame from window
        self.__configure()                          # initialize the look
        self.__widgets()                            # add widgets

    def __configure(self):
        """Initialize the look/location of the Form."""
        self.__frame.configure(background=self.COLOR)       # color
        self.__frame.place(relwidth=self.RELATIVE_WIDTH)    # span across
        self.__frame.place(relheight=self.RELATIVE_HEIGHT)  # span up/down

    def __widgets(self):
        """Create widgets contained in Form."""
        self.__micButton = MicButton(self.__frame)
        self.__fileButton = FileButton(self.__frame)

    def __setPlots(self, plots):
        """Pass plot object to widgets"""
        self.__micButton.plots = plots
        self.__fileButton.plots = plots
        pass

    """Property for setting plots widget."""
    plots = property(None, __setPlots)
