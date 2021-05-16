from patterns.singleton import Singleton            # design pattern (one instance)
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity
from gui.emotionForm import EmotionForm             # display emotion intensity
from predictions.predictorv0 import predict_emotion # predict emotion via sound file

class EmotionPredictor(object, metaclass=Singleton):
    def __init__(self):
        """Construct object."""
        self.__emotionForm = None
        self.__getEmotionForm()

    def predict(self, filename):
        """Predict emotion/intensity via convolutional neutal network."""
        # filename    sound file to be analyzed for emotion

        results = predict_emotion(filename)
        print(results)
        self.__updateEmotion()

    def __getEmotionForm(self):
        """Get the widget instance for diplaying emotion."""
        if self.__emotionForm is None:
            self.__emotionForm = EmotionForm.instance

    def __updateEmotion(self):
        """Set the emotion/intensity displayed."""
        self.__getEmotionForm()
        self.__emotionForm.emotion(Emotion.ANGRY)
        self.__emotionForm.intensity(Intensity.STRONG)
