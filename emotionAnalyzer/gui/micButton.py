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
        super().__init__(form=form, 
                        bTxt=self.BUTTON_TEXT, 
                        bCmd=lambda: self.__startMic())
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""
        self._button.configure(foreground=self.FOREGROUND)
        self._button.configure(background=self.BACKGROUND)

    def __startMic(self):
        """Open dialog window for finding/selecting file."""
        self._plots.processMic()                   # update plots with microphone
