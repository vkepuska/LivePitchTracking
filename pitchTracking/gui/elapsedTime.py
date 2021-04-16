import tkinter as tk                                # GUI toolkit


class ElapsedTime(object):
    """Class for dislaying elapsed processing time."""

    # Constants.
    UNIT = 'nano-seconds'                           # unit of time
    DEFAULT = 'TBD'                                 # value when none passed

    def __init__(self, win):
        """Construct object."""
        self.__frame = tk.Frame(win)                # create frame from window
        self.__lUnit = tk.Label(self.__frame, text=self.UNIT)   # unit label
        self.__lUnit.pack(side=tk.RIGHT)            # move to right in parent
        self.__time = tk.StringVar()                # static variable
        self.__time.set(self.DEFAULT)               # initialize variable
        # add value widget
        self.__lValue = tk.Label(self.__frame, textvariable=self.__time)
        self.__lValue.pack(side=tk.RIGHT)           # move to right in parent
        self.__frame.pack(anchor=tk.SE)             # bottom right
        self.__frame.pack(fill=tk.X)                # fill horizontally
        self.__frame.pack(expand=tk.YES)            # fill up space not used

    def __setTime(self, value=DEFAULT):
        """Set new elapsed time."""
        # value elapsed time

        self.__time.set(value)

    """Property for setting time value."""
    time = property(None, __setTime)
