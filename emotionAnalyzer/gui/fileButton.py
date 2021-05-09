import tkinter as tk                                # GUI toolkit
from gui.commandButton import CommandButton         # parent for press buttons
from tkinter.filedialog import askopenfilename      # creates file dialog
from samples.audioFile import AudioFile             # handle audio file

class FileButton(CommandButton):
    """Class for selecting sound file."""

    # Constants
    BUTTON_TEXT = 'FILE'                            # display text
    FOREGROUND = 'white'                            # text color
    BACKGROUND = 'blue'                             # button color
    OPEN_TITLE = 'Select sound file'                # user prompt
    FILE_TYPES = [("Wave files", "*.wav")]          # allowed file types
    ENTRY_BIND = '<Return>'                         # key press button
    PADX = 10                                       # 10 pixes between widget

    def __init__(self, form):
        """Construct object."""
        super().__init__()                          # call parent constructor
        self.__button = tk.Button(master=form,
                                  text=self.BUTTON_TEXT,
                                  command=lambda: self.__loadFile())
        self.__entryFile = tk.StringVar()           # static variable
        self.__audioFile = AudioFile()              # audio file handler
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Button."""

        self.__button.pack(side=tk.RIGHT)           # right justify
        self.__button.configure(font=self._font)
        self.__button.configure(foreground=self.FOREGROUND)
        self.__button.configure(background=self.BACKGROUND)

    def __loadFile(self):
        """Open dialog window for finding/selecting file."""
        value = askopenfilename(title=self.OPEN_TITLE,      # window title
                                filetypes=self.FILE_TYPES)  # allowed file type
        self.__entryFile.set(value)                  # update text box w/ name
        self.__processFile(value)                   # process w/ selected file

    def __OnFileEntryClick(self, event):
        """Callback when file is selected."""
        value = self.__entryFile.get().strip()      # extract whitespace
        self.__processFile(value)                   # process w/ selected file

    def __processFile(self, value):
        """Process selected file."""
        self.__audioFile.fileName = value           # inform audio file of name
        self._plots.processFile()                  # update plots with file
