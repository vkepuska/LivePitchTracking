from enum import Enum           # parent class that supports enum in python


class Emotion(Enum):
    """Enumerated list for emotion."""
    NEUTRAL     = 1             # no emotion detected
    CALM        = 2             # tranquil
    HAPPY       = 3             # cheerful
    SAD         = 4             # sorrowful
    ANGRY       = 5             # infuriated
    FEARFUL     = 6             # anxiety
    DISGUST     = 7             # revulsion
    SURPRISED   = 8             # astonished


class Intensity(Enum):
    """Enumerated list for emotional intensity."""
    NORMAL = 1                  # not loud
    STRONG = 2                  # loud
