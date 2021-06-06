from pathlib import Path                            # extension extraction
from tkinter import messagebox                      # error box
from patterns.singleton import Singleton            # design pattern (one instance)
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity
from gui.emotionForm import EmotionForm             # display emotion intensity
from predictions.predictorv0 import predict_emotion # predict emotion via sound file
from universal.constants import MODEL_FILE          # storage for model
from universal.constants import DEFAULT_EMOTION     # starting emotion
from universal.constants import DEFAULT_INTENSITY   # starting intensity

class EmotionPredictor(object, metaclass=Singleton):
    """Predicts emotions from sound file."""

    # Constants
    MODEL_EXT = '.model'
    KERAS_EXT = '.h5'

    def __init__(self):
        """Construct object."""
        self.__emotionForm = None
        self.__getEmotionForm()
        self.__kerasModel = None

    def predict(self, filename):
        """Predict emotion/intensity via convolutional neutal network."""
        # filename    sound file to be analyzed for emotion
        ext = Path(MODEL_FILE).suffix
        if ext == self.MODEL_EXT:
            self.__updateEmotion(predict_emotion(filename))
        elif ext == self.KERAS_EXT:
            # TODO: After merge of basicNN branch, integrate LivePredictions.make_predictions() functionality.
            messagebox.showerror(
                "Unsupported File", 'Code needs to be refactored to support {} type files!'.format(ext))
        else:
            messagebox.showerror(
                "Invalid Extension", '{} has an invalid extension for model files!'.format(ext))

    def __getEmotionForm(self):
        """Get the widget instance for diplaying emotion."""
        if self.__emotionForm is None:
            self.__emotionForm = EmotionForm.instance

    def __updateEmotion(self, results):
        """Set the emotion/intensity displayed."""
        # results    string of prediction from model
        self.__getEmotionForm()
        self.__emotionForm.emotion(self.__getEnum(Emotion, results, DEFAULT_EMOTION))
        self.__emotionForm.intensity(self.__getEnum(Intensity, results, DEFAULT_INTENSITY))

    def __getEnum(self, enum, text, default):
        """Get the emotion for results string."""
        # enum      enumerated list
        # text      string that should match an enumeration
        for e in enum:
            if text.lower() == e.name.lower():
                return e
        return default

