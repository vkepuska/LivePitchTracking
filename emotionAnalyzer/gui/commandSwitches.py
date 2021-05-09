import tkinter as tk                            # GUI toolkit
from patterns.singleton import Singleton        # design pattern (one instance)


class CommandSwitch(object, metaclass=Singleton):
    """Genralized class for toggle switches in the GUI."""

    # Constants
    COLOR = 'black'                             # color of toggle switch
    TEXT_COLOR = 'white'                        # color of text in switch
    SELECT_COLOR = 'grey'                       # color while selected
    MODE = 1                                    # default mode to start with
    PADX = 10                                   # 10 pixes between widget

    def __init__(self, form, modes, color=COLOR, default=MODE):
        """Construct object."""
        # form      widget to place switch into
        # modes     enumerated list of possible modes
        # color     toggle switch color
        # default   mode to start display with

        self.__frame = tk.Frame(form)           # create frame widge from form
        self.__mode = tk.IntVar(form, default)  # static variable holds value
        self.buttons = dict()                   # container for button widgets
        for mode in modes:                                  # itterate modes
            button = tk.Radiobutton(master=self.__frame)    # parent widget
            button.config(text=mode.name)                   # button  text
            button.config(variable=self.__mode)             # switch var
            button.config(value=mode.value)                 # switch value
            button.config(indicatoron=False)                # raised/sunken
            button.config(background=color)                 # set color
            button.config(foreground=self.TEXT_COLOR)       # text color
            button.config(selectcolor=self.SELECT_COLOR)    # selected color
            button.pack(side=tk.LEFT)                       # next left
            self.buttons.update({mode.name: button})        # btn container
        self.__frame.pack(side=tk.LEFT)         # place left edge of figure
        self.__frame.pack(padx=self.PADX)       # space between widget l/r

    @property
    def mode(self):
        """Return current mode of switch."""
        return self.__mode.get()

    @mode.setter
    def mode(self, value):
        """Set new mode of switch."""
        self.__mode.set(value)
