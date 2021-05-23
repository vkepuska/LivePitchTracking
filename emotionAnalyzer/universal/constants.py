from enumerations.emotions import Emotion
from enumerations.emotions import Intensity

# constant values
FS = 16000                                  # sampling frequency (Hz)
FRAME_PERIOD = 100                          # time (ms) in analysis window
NUM_CHANNELS = 1                            # 1=monoaural, 2=stereophonic
DATA_TYPE = 'int16'                         # sample type (16-bit integer)
RECORDING = 'recording'                     # name of folder to hold recording
FILE_NAME_PREFIX = 'SAE'                    # designater for recording from app
RECORDING_LENGTH = 5                        # seconds to record using mic

# calculated values
FRAME_DURATION = FRAME_PERIOD / 1000        # fraction of second for frame
FRAME_LENGTH = round(FRAME_DURATION * FS)   # num samples in analysis window

# defaults
DEFAULT_EMOTION = Emotion.NEUTRAL           # emotion to load at start
DEFAULT_INTENSITY = Intensity.NORMAL        # intensity to load at start
