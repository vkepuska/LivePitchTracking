import tkinter as tk                                # GUI toolkit
from gui.commandButton import CommandButton         # parent for press buttons
from tkinter.filedialog import askopenfilename      # creates file dialog

class MicButton(CommandButton):
    """Class for selecting sound file."""

    # Constants
    FOREGROUND = 'white'                            # text color
    START_TEXT = 'START'                            # text to start microphone
    START_COLOR = 'green'                           # star button color
    STOP_TEXT = 'STOP'                              # text to start microphone
    STOP_COLOR = 'red'                              # stop button color

    def __init__(self, form):
        """Construct object."""
        super().__init__(form=form, 
                         bTxt=self.START_TEXT,
                         bCmd=lambda: self.__toggleMic())
        self.__start = True
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""
        self._button.configure(foreground=self.FOREGROUND)
        self._button.configure(background=self.START_COLOR)

    def __toggleMic(self):
        """Toggle the microphone button to start/stop it."""
        if self.__start:
            self._button['text'] = self.STOP_TEXT
            self._button.configure(background=self.STOP_COLOR)
            self._plots.processMic()                # update plots with microphone
            self.__start = False
        else:
            self._button['text'] = self.START_TEXT
            self._button.configure(background=self.START_COLOR)
            self._plots.stopMic()                   # stop updating the microphone
            self.__start = True
