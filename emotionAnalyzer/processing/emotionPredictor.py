from patterns.singleton import Singleton            # design pattern (one instance)
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity
from gui.emotionForm import EmotionForm             # display emotion intensity
#from predictions.predictorv0 import predict_emotion

class EmotionPredictor(object, metaclass=Singleton):
    def __init__(self):
        self.__emotionForm = None
        self.__getEmotionForm()

    def predict(self, filename):
        #results = predict_emotion(filename)
        #print(results)
        self.__updateEmotion()

    def __getEmotionForm(self):
        if self.__emotionForm is None:
            self.__emotionForm = EmotionForm.instance

    def __updateEmotion(self):
        self.__getEmotionForm()
        self.__emotionForm.emotion(Emotion.ANGRY)
        self.__emotionForm.intensity(Intensity.STRONG)
