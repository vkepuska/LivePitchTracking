import tkinter as tk                            # GUI toolkit
from patterns.singleton import Singleton        # design pattern (one instance)
import tkinter.font as font                     # font parameters


class CommandButton(object, metaclass=Singleton):
    """Genralized class for buttons in the GUI."""

    # Constants
    FONT_FAMILY = 'Helvetica'                       # font used
    FONT_SIZE = 30                                  # size of font
    FONT_WEIGHT = 'bold'                            # boldface or normal

    def __init__(self, form, bTxt, bCmd):
        """Construct object."""
        self._button = tk.Button(master=form, text=bTxt, command=bCmd)
        self.__plots = None                         # plots to process file
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""
        # text box entry widget
        self.__font = font.Font(family=self.FONT_FAMILY, 
                                size=self.FONT_SIZE, 
                                weight=self.FONT_WEIGHT)
        self._button.configure(font=self._font)    # set common font

    @property
    def _font(self):
        """Getter for font parameters."""
        return self.__font

    @property
    def _plots(self):
        """Getter for plots object."""
        return self.__plots

    def __setPlots(self, widget):
        """Set plot widget."""
        self.__plots = widget

    """Property for setting plots widget."""
    plots = property(None, __setPlots)

    def relx(self,value):
        "Set relative horizontal offset from parent widget."
        self._button.place(relx=value)

    def rely(self, value):
        "Set relative vertical offset from parent widget."
        self._button.place(rely=value)

    def relwidth(self, value):
        "Set relative width within parent widget."
        self._button.place(relwidth=value)

    def relheight(self, value):
        "Set relative height within parent widget."
        self._button.place(relheight=value)
