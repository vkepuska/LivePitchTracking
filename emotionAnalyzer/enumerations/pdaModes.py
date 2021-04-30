from enum import Enum           # parent class that supports enum in python


class InputSources(Enum):
    """Enumerated list for possible sound input sources."""
    MIC = 1                     # stream data from microphone
    FILE = 2                    # read data from selected sound file


class DisplayPlots(Enum):
    """Enumerated list for possible sound input sources."""
    NONE = 1                    # don't show any type of plot
    MAGNITUDE = 2               # show amplitude of sound wave
    FREQUENCY = 3               # show spectrograph of sound
    PITCH = 4                   # show pitch plot of sound
    ALL = 5                     # show all (mag, freq, and pitch)
