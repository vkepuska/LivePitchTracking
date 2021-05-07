import numpy as np                              # library to convert data
from patterns.singleton import Singleton        # design pattern (one instance)
from universal.constants import FS              # sampling frequency
from universal.constants import FRAME_LENGTH    # analysis window
from universal.constants import NUM_CHANNELS    # audio channels
from universal.constants import DATA_TYPE       # sample type


class Microphone(object, metaclass=Singleton):
    """Handles microphone access."""

    # Constants
    INPUT = True                                # input stream

    def __init__(self):
        """Construct object."""
        try:
            import pyaudio as pa                # API to access mic stream
        except ImportError:
            import stub.pyaudio as pa           # temporary stub till work on Android
        self.FORMAT = pa.paInt16                # data type
        self.__audio = pa.PyAudio()             # microphone object
        self.__stream = None                    # stream object
        self.__buffer = np.zeros(FS)            # store 1 sec of samples

    def __del__(self):
        """Destrory object."""
        self.__buffer = None                    # empty array
        if self.__stream is not None:           # was stream openned
            self.__stream.stop_stream()         # stop collecting samples
            self.__stream.close()               # delete the stream
        self.__audio.terminate()                # delete the microphone object

    def open(self):
        """Open stream from microphone."""
        if self.__stream is None:
            self.__open()                       # instantiate stream object
        else:
            self.__stream.start_stream()        # reactivate collecting samples

    def run(self):
        """Extract sound samples from micophone."""
        raw = self.__stream.read(FRAME_LENGTH, False)   # get frame of mic samples
        data = np.fromstring(raw, DATA_TYPE)    # convert mic samples to type
        n = len(data)                           # number of samples
        self.__buffer[0:FS-n] = self.__buffer[n:]     # shift old forward
        self.__buffer[FS-n:] = data             # append new data
        return True                             # ran fine

    def close(self):
        """Close file."""
        self.__buffer = np.zeros(FS)            # clear buffer
        self.__stream.stop_stream()             # deactivate sample collection

    @property
    def data(self):
        """Get data samples."""
        return self.__buffer                    # buffer of mic samples

    def __open(self):
        """Instantiate stream object."""
        self.__stream = self.__audio.open(      # open microphone stream
            format=self.FORMAT,                 # sampling format
            channels=NUM_CHANNELS,              # number of audio channels
            rate=FS,                            # sampling rate
            input=self.INPUT,                   # input stream (mic->program)
            frames_per_buffer=FRAME_LENGTH)     # number of frames in buffer
