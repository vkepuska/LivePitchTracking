import tkinter as tk                                # GUI toolkit
from tkinter.filedialog import askopenfilename      # creates file dialog
from samples.audioFile import AudioFile             # handle audio file


class FileButton(object):
    """Class for selecting sound file."""

    # Constants
    BUTTON_TEXT = 'FILE'                          # display text
    OPEN_TITLE = 'Select sound file'                # user prompt
    FILE_TYPES = [("Wave files", "*.wav")]          # allowed file types
    ENTRY_BIND = '<Return>'                         # key press button
    PADX = 10                                       # 10 pixes between widget

    def __init__(self, form):
        """Construct object."""
        self.__frame = tk.Frame(form)               # create frame widge
        self.__audioFile = AudioFile()              # audio file handler
        self.__plots = None                         # plots to process file

        # text box entry widget
        self.__entryFile = tk.StringVar()           # static variable

        # file dialog button
        self.__button = tk.Button(master=self.__frame,      # parent widget
                                  text=self.BUTTON_TEXT,    # display text
                                  command=lambda: self.__loadFile())  # calback
        self.__button.pack(side=tk.LEFT)            # move to left of parent

        # move widgets within parent
        self.__frame.pack(side=tk.LEFT)             # move to left of parent
        self.__frame.pack(padx=self.PADX)           # space between widget l/r
        self.__frame.pack(fill=tk.X)                # fill horizontal
        self.__frame.pack(expand=tk.YES)            # fill extra window space

    def __setPlots(self, widget):
        """Set plot widget."""
        self.__plots = widget

    """Property for setting plots widget."""
    plots = property(None, __setPlots)

    def __loadFile(self):
        """Open dialog window for finding/selecting file."""
        value = askopenfilename(title=self.OPEN_TITLE,      # window title
                                filetypes=self.FILE_TYPES)  # allowed file type
        self.__entryFile.set(value)                 # update text box w/ name
        self.__processFile(value)                   # process w/ selected file

    def __OnFileEntryClick(self, event):
        """Callback when file is selected."""
        value = self.__entryFile.get().strip()      # extract whitespace
        self.__processFile(value)                   # process w/ selected file

    def __processFile(self, value):
        """Process selected file."""
        self.__audioFile.fileName = value           # inform audio file of name
        self.__plots.processFile()                  # update plots with file
