from enumerations.emotions import Emotion
from enumerations.emotions import Intensity

# audio
FS = 44100                                  # sampling frequency (Hz)
FRAME_PERIOD = 10                           # time (ms) in analysis window
NUM_CHANNELS = 1                            # 1=monoaural, 2=stereophonic
DATA_TYPE = 'int16'                         # sample type (16-bit integer)
RECORDING = 'recording'                     # name of folder to hold recording
FILE_NAME_PREFIX = 'SAE'                    # designater for recording from app
RECORDING_LENGTH = 3                        # seconds to record using mic
FRAMES_PER_BUFFER = 1024                    # number of frames per buffer

# model
#MODEL_FILE = 'predictions/basic.model'
MODEL_FILE = 'models/Emotion_Voice_Detection_Modelv6.h5'

# defaults emotions
DEFAULT_EMOTION = Emotion.NEUTRAL           # emotion to load at start
DEFAULT_INTENSITY = Intensity.NORMAL        # intensity to load at start
