import tkinter as tk                                # GUI toolkit
from gui.commandButton import CommandButton         # parent for press buttons
from tkinter.filedialog import askopenfilename      # creates file dialog

class MicButton(CommandButton):
    """Class for selecting sound file."""

    # Constants
    BUTTON_TEXT = 'START'                           # display text
    FOREGROUND = 'white'                            # text color
    BACKGROUND = 'green3'                           # button color
    PADX = 10                                       # 10 pixes between widget

    def __init__(self, form):
        """Construct object."""
        super().__init__()                          # call parent constructor
        self.__frame = tk.Frame(form)               # create frame widge
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""
        # file dialog button
        self.__button = tk.Button(master=self.__frame,      # parent widget
                                  text=self.BUTTON_TEXT,    # display text
                                  command=lambda: self.__startMic())  # calback
        self.__button.pack(side=tk.LEFT)            # move to right
        self.__button.configure(font=self._font)
        self.__button.configure(foreground=self.FOREGROUND)
        self.__button.configure(background=self.BACKGROUND)
        self.__frame.pack(side=tk.LEFT)            # move to right of parent
        self.__frame.pack(padx=self.PADX)           # space between widget l/r

    def __startMic(self):
        """Open dialog window for finding/selecting file."""
        self._plots.processMic()                   # update plots with microphone
