from patterns.singleton import Singleton            # design pattern (one instance)
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity
from gui.emotionForm import EmotionForm             # display emotion intensity

class EmotionPredictor(object, metaclass=Singleton):
    def __init__(self):
        self.__emotionForm = None
        self.__getEmotionForm()

    def __getEmotionForm(self):
        if self.__emotionForm is None:
            self.__emotionForm = EmotionForm.instance

    def predict(self, file):
        self.__getEmotionForm()
        self.__emotionForm.emotion(Emotion.ANGRY)
        self.__emotionForm.intensity(Intensity.STRONG)
