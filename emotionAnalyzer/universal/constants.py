# constant values
FS = 16000                                  # sampling frequency (Hz)
FRAME_PERIOD = 100                          # time (ms) in analysis window
NUM_CHANNELS = 1                            # 1=monoaural, 2=stereophonic
DATA_TYPE = 'int16'                         # sample type (16-bit integer)

# calculated values
FRAME_DURATION = FRAME_PERIOD / 1000        # fraction of second for frame
FRAME_LENGTH = round(FRAME_DURATION * FS)   # num samples in analysis window

# default window size
DEFAULT_WINDOW_WIDTH = 480                  # pixels across
DEFAULT_WINDOW_HEIGHT = 800                 # pixels up/down

class WINDOW(object):
    def __init__(self):
        self.__width = DEFAULT_WINDOW_WIDTH
        self.__height = DEFAULT_WINDOW_HEIGHT

    
