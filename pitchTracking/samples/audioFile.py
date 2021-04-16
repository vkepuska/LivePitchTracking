from os import path as fileSystem               # file system from OS
import wave as wav                              # API to access WAV files
import numpy as np                              # library to convert data
from patterns.singleton import Singleton        # design pattern (one instance)
from universal.constants import NUM_CHANNELS    # number of audio channels
from universal.constants import DATA_TYPE       # type of samples values


class AudioFile(object, metaclass=Singleton):
    """Handles audio file access."""

    # Constants
    OPEN_MODE = 'r'                             # read only
    NUM_FRAMES = -1                             # all frames in file
    OPEN_ERROR = 'Error reading the audio file. ' \
        'Only WAV files are supported.'         # message when file can't open

    def __init__(self):
        """Construct object."""
        self.__fileName = None                  # audio file path/name
        self.__raw = None                       # audio file object
        self.__data = None                      # processed audio samples
        self.__rate = None                      # sampling rate from file

    def open(self):
        """Open file."""
        if not self.__isValidFile():            # file is invalid
            return                              # exit early
        try:                                    # test code block
            # extract file data
            self.__raw = wav.open(self.__fileName, self.OPEN_MODE)
        except (wav.Error, EOFError):           # handle error
            raise OSError(self.OPEN_ERROR)      # upable to open file

    def run(self):
        """Extract sound samples from file."""
        if not self.__isValidFile():            # file is invalid
            return                              # exit early
        # only process data with specific number of channels
        if self.__raw.getnchannels() != NUM_CHANNELS:
            return False                        # too many channels, exit early
        # extract specific number of frames from file
        signal = self.__raw.readframes(self.NUM_FRAMES)
        # convert frames to specific data type
        self.__data = np.frombuffer(signal, dtype=DATA_TYPE)
        # store sampling rate of file
        self.__rate = self.__raw.getframerate()
        return True                             # ran okay

    def close(self):
        """Close file."""
        if self.__raw is not None:              # check if file object exists
            self.__raw.close()                  # object exists, close it

    def __setFileName(self, fileName):
        """Sets name of audio file."""
        # fileName  name of file

        self.__fileName = fileName              # store audio file name

    def __isValidFile(self):
        """Checks for file validity."""
        if self.__fileName is None:             # file name not set
            return False                        # no file name, invalid
        if not fileSystem.isfile(self.__fileName):  # path/file exists?
            return False                        # no file, invalid
        return True                             # good file, valid

    """Property for setting file name."""
    fileName = property(None, __setFileName)

    @property
    def data(self):
        """Return data samples."""
        return self.__data

    @property
    def rate(self):
        """Return sample rate."""
        return self.__rate
