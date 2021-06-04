from os import path                             # check for existing folder
from os import mkdir                            # make new folder
from datetime import datetime                   # current date/time
import pyaudio as pa                            # API to access mic stream
import wave as wav                              # API to access WAV files
import numpy as np                              # library to convert data
from patterns.singleton import Singleton        # design pattern (one instance)
from universal.constants import FS              # sampling frequency
from universal.constants import FRAMES_PER_BUFFER   # analysis window
from universal.constants import NUM_CHANNELS    # audio channels
from universal.constants import DATA_TYPE       # sample type
from universal.constants import RECORDING       # folder to store samples
from universal.constants import FILE_NAME_PREFIX    # recording files from app
from universal.constants import RECORDING_LENGTH    # seconds to record at time
from processing.emotionPredictor import EmotionPredictor    # predicts emotion

class Microphone(object, metaclass=Singleton):
    """Handles microphone access."""

    # Constants
    INPUT = True                                # input stream
    OPEN_MODE = 'wb'                            # write only

    def __init__(self):
        """Construct object."""
        self.FORMAT = pa.paInt16                # data type
        self.__audio = pa.PyAudio()             # microphone object
        self.__stream = None                    # stream object
        self.__buffer = np.zeros(FS)            # store 1 sec of samples
        # wrapper to process emotion and display it
        self.__emotionPredictor = EmotionPredictor()
        self.__sampleFile = None                # file for recordings
        self.__recorded = 0                     # number of samples recorded

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
        self.__stream.start_stream()            # reactivate collecting samples

    def run(self):
        """Extract sound samples from micophone."""
        # get frame of mic samples
        if self.__stream is None:
            # callin code needs to open stream 1st
            return False
        else:
            # wait for sufficient sample, else pitch plot crashes
            if self.__recorded >= FRAMES_PER_BUFFER:
                # new file if time exceeded
                self.__openSampleFile()
                return True
            else:
                # not enough samples
                return False

    def __openSampleFile(self):
        """Open a sample file and if duration exceeded, create new one."""
        if self.__sampleFile is None:
            # create new time stamped file
            self.__newSampleFile()
        else:
            # check for duration of recording to start new upon time exceeded
            duration = self.__sampleFile.getnframes() / float(FS)
            if duration >= RECORDING_LENGTH:
                self.__stream.stop_stream()             # deactivate sample collection
                self.__sampleFile.close()               # close latest file
                # update prediction
                self.__emotionPredictor.predict(self.__fileName)
                self.__stream.start_stream()            # reactivate sample collection
                self.__newSampleFile()                  # create new file for more recording
                self.__recorded = 0                     # wait for sufficient recording

    def __newSampleFile(self):
        """Create new sample recording file."""
        self.__newFileName()
        self.__sampleFile = wav.open(self.__fileName, self.OPEN_MODE)
        self.__sampleFile.setnchannels(NUM_CHANNELS)
        self.__sampleFile.setsampwidth(self.__audio.get_sample_size(self.FORMAT))
        self.__sampleFile.setframerate(FS)

    def __save(self,audio):
        """Save audio data to sample file."""
        self.__openSampleFile()
        self.__sampleFile.writeframes(audio)

    def __newFileName(self):
        """Create new sample file name per date/time."""
        now = datetime.now()
        dateTimeAppend = now.strftime('%y%m%d_%H%M%S')
        self.__fileName = '{}/{}_{}.wav'.format(RECORDING,
                                         FILE_NAME_PREFIX, 
                                         dateTimeAppend)

    def close(self):
        """Close file."""
        self.__buffer = np.zeros(FS)            # clear buffer
        self.__stream.stop_stream()             # deactivate sample collection
        self.__stream.close()
        self.__stream = None
        self.__emotionPredictor.predict(self.__fileName)
        self.__sampleFile.close()
        self.__sampleFile = None

    @property
    def data(self):
        """Get data samples."""
        return self.__buffer                    # buffer of mic samples

    @property
    def enabled(self):
        """Determined if microphone is enabled."""
        return True

    def __open(self):
        """Instantiate stream object."""
        if not path.exists(RECORDING):              # make recoding folder if needed
            mkdir(RECORDING)             
        if self.__sampleFile is None:               # make new recording file
            self.__newSampleFile()
        self.__stream = self.__audio.open(          # open microphone stream
            format=self.FORMAT,                     # sampling format
            channels=NUM_CHANNELS,                  # number of audio channels
            rate=FS,                                # sampling rate
            input=self.INPUT,                       # input stream (mic->program)
            frames_per_buffer=FRAMES_PER_BUFFER,    # number of frames in buffer
            stream_callback=self.get_callback())    # callback to record audio

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.__sampleFile.writeframes(in_data)      # update wavefile
            data = np.fromstring(in_data, dtype=np.int16)   # plots need int
            n = len(data)                               # number of samples
            self.__buffer[0:FS-n] = self.__buffer[n:]   # shift old forward
            self.__buffer[FS-n:] = data                 # append new data
            self.__recorded += n                        # track length samples
            return in_data, pa.paContinue
        return callback
