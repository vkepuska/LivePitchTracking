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
        self.__button = tk.Button(master=form,
                                  text=self.BUTTON_TEXT,
                                  command=lambda: self.__startMic())
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""
        self.__button.pack(side=tk.LEFT)            # move to left of parent
        self.__button.configure(font=self._font)    # set common font
        self.__button.configure(foreground=self.FOREGROUND)
        self.__button.configure(background=self.BACKGROUND)

    def __startMic(self):
        """Open dialog window for finding/selecting file."""
        self._plots.processMic()                   # update plots with microphone
