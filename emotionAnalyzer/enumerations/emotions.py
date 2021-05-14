from enum import Enum           # parent class that supports enum in python


class Emotion(Enum):
    """Enumerated list for emotion."""
    NEUTRAL     = 0             # no emotion detected
    CALM        = 1             # tranquil
    HAPPY       = 2             # cheerful
    SAD         = 3             # sorrowful
    ANGRY       = 4             # infuriated
    FEARFUL     = 5             # anxiety
    DISGUST     = 6             # revulsion
    SURPRISED   = 7             # astonished


class Intensity(Enum):
    """Enumerated list for emotional intensity."""
    NORMAL = 0                  # not loud
    STRONG = 1                  # loud
