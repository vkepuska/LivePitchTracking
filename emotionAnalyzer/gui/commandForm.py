import tkinter as tk                                # GUI toolkit
from gui.micButton import MicButton                 # button to start microphone
from gui.fileButton import FileButton               # button to select file


class CommandForm(object):
    """Manages the window form for controlling the GUI."""

    COLOR = 'gray'                                  # background color
    RELATIVE_WIDTH = 1.0                            # entire width
    RELATIVE_HEIGHT = 0.1                           # top 0.1 of window
    MIC_RELX = 0.0                                  # far left
    MIC_RELY = 0.0                                  # top
    MIC_RELW = 0.5                                  # span half across
    MIC_RELH = 1.0                                  # span entire up/down
    FILE_RELX = 0.5                                 # half way across
    FILE_RELY = 0.0                                 # top
    FILE_RELW = 0.5                                 # span half across
    FILE_RELH = 1.0                                 # span entire up/down

    def __init__(self, win):
        """Construct object."""
        # win   window application

        self.__frame = tk.Frame(win)                # create frame from window
        self.__widgets()                            # add widgets
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Form."""
        self.__frame.configure(background=self.COLOR)       # color
        self.__frame.place(relwidth=self.RELATIVE_WIDTH)    # span across
        self.__frame.place(relheight=self.RELATIVE_HEIGHT)  # span up/down
        self.__micButton.relx(self.MIC_RELX)
        self.__micButton.rely(self.MIC_RELY)
        self.__micButton.relwidth(self.MIC_RELW)
        self.__micButton.relheight(self.MIC_RELH)
        self.__fileButton.relx(self.FILE_RELX)
        self.__fileButton.rely(self.FILE_RELY)
        self.__fileButton.relwidth(self.FILE_RELW)
        self.__fileButton.relheight(self.FILE_RELH)

    def __widgets(self):
        """Create widgets contained in Form."""
        self.__micButton = MicButton(self.__frame)
        self.__fileButton = FileButton(self.__frame)

    def __setPlots(self, plots):
        """Pass plot object to widgets"""
        self.__micButton.plots = plots
        self.__fileButton.plots = plots

    """Property for setting plots widget."""
    plots = property(None, __setPlots)
