import tkinter as tk                                # GUI toolkit
from universal.constants import PROCESS_FILE        # allow user process files
from gui.displaySwitch import DisplaySwitch         # switch for plot to display
from gui.sourceSwitch import SourceSwitch           # source input switch
from gui.fileBrowser import FileBrowser             # select sound file
from gui.fileButton import FileButton


class CommandForm(object):
    """Manages the window form for controlling the GUI."""

    def __init__(self, win):
        """Construct object."""
        # win   window application

        self.__frame = tk.Frame(win)                # create frame from window
        # create widges
        #self.__displaySwitch = DisplaySwitch(self.__frame)      # plot select
        #if(PROCESS_FILE):                                       # file process
            #self.__sourceSwitch = SourceSwitch(self.__frame)    # input select
            #self.__fileBrowser = FileBrowser(self.__frame)      # file bowser
        self.__fileButton = FileButton(self.__frame)
        # place form within window
        self.__frame.pack(anchor=tk.N)              # center top
        self.__frame.pack(fill=tk.X)                # fill horizontally
        self.__frame.pack(expand=tk.YES)            # fill up space not used

    def __setPlots(self, plots):
        """Passes plot object to widgets"""
        # plots widget that handles plits

        # pass plots to other widgets for callbacks
        #self.__displaySwitch.plots = plots          # plot select
        #if(PROCESS_FILE):                           # file process
            #self.__fileBrowser.plots = plots        # file browser
            #self.__sourceSwitch.plots = plots       # input source
        self.__fileButton.plots = plots

    """Property for setting plots widget."""
    plots = property(None, __setPlots)
