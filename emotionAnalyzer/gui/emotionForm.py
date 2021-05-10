import tkinter as tk                                # GUI toolkit
import tkinter.font as font                     # font parameters
from PIL import ImageTk
from PIL import Image
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity


class EmotionForm(object):
    """Manages the window form for controlling the GUI."""

    # Constants
    FONT_FAMILY = 'Helvetica'                   # font used
    FONT_SIZE = 16                              # size of font
    FONT_WEIGHT = 'bold'                        # boldface or normal
    COLOR = 'snow3'                             # background color
    RELX = 0.0                                  # far left
    RELY = 0.8                                  # near bottom
    RELW = 1.0                                  # span across
    RELH = 0.2                                  # span last segment
 
    # emotion
    NEUTRAL = 'image/neutral.png' 
    CALM = 'image/calm.png'
    HAPPY = 'image/happy.png'
    SAD = 'image/sad.png' 
    ANGRY = 'image/angry.png' 
    FEARFUL = 'image/fearful.png'
    DISGUST = 'image/disgust.png'
    SURPRISED = 'image/suprised.png'
    # intensity
    NORMAL = 'image/normal.png'
    STRONG = 'image/strong.png'

    def __init__(self, win):
        """Construct object."""
        # win   window application
        self.__frame = tk.Frame(win)                # create frame from window
        self.__loadEmotions()
        self.__loadIntensity()
        self.__widgets()                            # add widgets
        self.__configure()                          # initialize the look

    def __configure(self):
        """Initialize the look/location of the Form."""
        self.__frame.configure(background=self.COLOR)
        self.__frame.place(relx=self.RELX)
        self.__frame.place(rely=self.RELY)
        self.__frame.place(relwidth=self.RELW)
        self.__frame.place(relheight=self.RELH)

    def __loadEmotions(self):
        self.__emotion = []
        self.__emotion.insert(Emotion.NEUTRAL.value-1,
                            ImageTk.PhotoImage(Image.open(self.NEUTRAL)))
        self.__emotion.insert(Emotion.CALM.value-1,
                            ImageTk.PhotoImage(Image.open(self.CALM)))
        self.__emotion.insert(Emotion.HAPPY.value-1,
                            ImageTk.PhotoImage(Image.open(self.HAPPY)))
        self.__emotion.insert(Emotion.SAD.value-1,
                            ImageTk.PhotoImage(Image.open(self.SAD)))
        self.__emotion.insert(Emotion.ANGRY.value-1,
                            ImageTk.PhotoImage(Image.open(self.ANGRY)))
        self.__emotion.insert(Emotion.FEARFUL.value-1,
                            ImageTk.PhotoImage(Image.open(self.FEARFUL)))
        self.__emotion.insert(Emotion.DISGUST.value-1,
                            ImageTk.PhotoImage(Image.open(self.DISGUST)))
        self.__emotion.insert(Emotion.SURPRISED.value-1,
                            ImageTk.PhotoImage(Image.open(self.SURPRISED)))

    def __loadIntensity(self):
        self.__intensity = []
        self.__intensity.insert(Intensity.NORMAL.value,
                              ImageTk.PhotoImage(Image.open(self.NORMAL)))
        self.__intensity.insert(Intensity.STRONG.value,
                              ImageTk.PhotoImage(Image.open(self.STRONG)))

    def __widgets(self):
        """Create widgets contained in Form."""
        self.__emotionIcon = tk.Label(self.__frame,
                                   image=self.__emotion[Emotion.NEUTRAL.value-1])
        self.__emotionIcon.pack(side=tk.LEFT)

        self.__intensityIcon = tk.Label(self.__frame,
                              image=self.__intensity[Intensity.NORMAL.value-1])
        self.__intensityIcon.pack(side=tk.LEFT)

        self.__font = font.Font(family=self.FONT_FAMILY,
                                size=self.FONT_SIZE,
                                weight=self.FONT_WEIGHT)
        self.__emotionFrame = tk.Frame(self.__frame)
        self.__emotionFrame.pack(side=tk.TOP)
        self.__emotionText = tk.Label(self.__emotionFrame, text='Emotion: ')
        self.__emotionText.grid(row=0,column=0)
        self.__emotionText.configure(font=self.__font)
        self.__intensityText = tk.Label(self.__emotionFrame, text='Intensity: ')
        self.__intensityText.grid(row=1, column=0)
        self.__intensityText.configure(font=self.__font)
