# constant values
FS = 16000                                  # sampling frequency (Hz)
FRAME_PERIOD = 100                          # time (ms) in analysis window
HOP_PERIOD = 20                             # time between successive frames
NUM_CHANNELS = 1                            # 1=monoaural, 2=stereophonic
DATA_TYPE = 'int16'                         # sample type (16-bit integer)
PROCESS_FILE = False                        # allow user to process files

# calculated values
FRAME_DURATION = FRAME_PERIOD / 1000        # fraction of second for frame
FRAME_LENGTH = round(FRAME_DURATION * FS)   # num samples in analysis window
HOP_DURATION = HOP_PERIOD / 1000            # fraction of second for hops
HOP_LENGTH = round(HOP_DURATION * FS)       # num samples in successive frames
