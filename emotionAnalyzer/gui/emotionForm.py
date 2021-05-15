import tkinter as tk                                # GUI toolkit
import tkinter.font as font                         # font parameters
from PIL import ImageTk
from PIL import Image
from universal.constants import WINDOW_HEIGHT
from universal.constants import WINDOW_WIDTH
from enumerations.emotions import Emotion           # available emotions
from enumerations.emotions import Intensity         # available intensity


class EmotionForm(object):
    """Manages the window form for controlling the GUI."""

    # Constants
    FONT_FAMILY = 'Helvetica'                   # font used
    FONT_SIZE = 12                              # size of font
    FONT_WEIGHT = 'bold'                        # boldface or normal
    COLOR = 'snow3'                             # background color
    RELX = 0.0                                  # far left
    RELY = 0.7                                  # near bottom
    RELW = 1.0                                  # span across
    RELH = 0.3                                  # span last segment
    FOLDER = 'image/'                           # location of emoticons
    EXTENSION = '.png'                          # image type extension
    DEFAULT_EMOTION = Emotion.NEUTRAL           # emotion to load at start
    DEFAULT_INTENSITY = Intensity.NORMAL        # intensity to load at start
    FRAME_W = 0.5                               # split boundary in half for type
    FRAME_RELY = 0.0                            # start from top within e/i frame
    FRAME_RELX_E = 0.0                          # emotion is on left
    FRAME_RELX_I = 0.5                          # intensity is on right
    FRAME_TEXT_H = 0.1                          # text is 10% of e/i frame
    FULL_H = 1.0                                # full height is 100%

    def __init__(self, win):
        """Construct object."""
        # win   window application
        self.__frame = tk.Frame(win)                # create frame from window
        self.__loadEmotions()                       # add emotion icons
        self.__loadIntensity()                      # add intensity icons
        self.__widgets()                            # add widgets
        self.__configure()                          # initialize the look
        self.__setDefault()                         # startup values

    def __configure(self):
        """Initialize the look/location of the Form."""
        self.__frame.configure(background=self.COLOR)
        self.__frame.place(relx=self.RELX)
        self.__frame.place(rely=self.RELY)
        self.__frame.place(relwidth=self.RELW)
        self.__frame.place(relheight=self.RELH)

    def __setDefault(self):
        """Set default text and icon for startup."""
        self.emotion(self.DEFAULT_EMOTION)
        self.intensity(self.DEFAULT_INTENSITY)

    def emotion(self, emotion):
        """Set emotion text and icon."""
        text = 'Emotion: {}'.format(emotion.name)
        self.__emotionText.configure(text=text)
        self.__emotionIcon.configure(image=self.__emotion[emotion.value])


    def intensity(self, intensity):
        """Set emotion text and icon."""
        text = 'Intensity: {}'.format(intensity.name)
        self.__intensityText.configure(text=text)
        self.__intensityIcon.configure(image=self.__intensity[intensity.value])

    def __insert(self,container,icon):
        """Insert images into container"""
        img = Image.open(self.FOLDER+icon.name+self.EXTENSION)
        # span half of window
        imgWidth = int(WINDOW_WIDTH/2.0)
        # try to span e/i frame
        imgHeight = int(WINDOW_HEIGHT*(self.RELH*(1-self.FRAME_TEXT_H)))
        resizedImg = img.resize((imgWidth, imgHeight), Image.ANTIALIAS)
        container.insert(icon.value, ImageTk.PhotoImage(resizedImg))

    def __loadEmotions(self):
        """Load emotion images into container."""
        self.__emotion = []
        self.__insert(self.__emotion, Emotion.NEUTRAL)
        self.__insert(self.__emotion, Emotion.CALM)
        self.__insert(self.__emotion, Emotion.HAPPY)
        self.__insert(self.__emotion, Emotion.SAD)
        self.__insert(self.__emotion, Emotion.ANGRY)
        self.__insert(self.__emotion, Emotion.FEARFUL)
        self.__insert(self.__emotion, Emotion.DISGUST)
        self.__insert(self.__emotion, Emotion.SUPRISED)

    def __loadIntensity(self):
        """Load intensity images into container."""
        self.__intensity = []
        self.__insert(self.__intensity, Intensity.NORMAL)
        self.__insert(self.__intensity, Intensity.STRONG)

    def __widgets(self):
        """Create widgets contained in Form."""
        self.__text()
        self.__emodicons()

    def __text(self):
        """Configure the e/i descriptions."""
        self.__font = font.Font(family=self.FONT_FAMILY,
                                size=self.FONT_SIZE, 
                                weight=self.FONT_WEIGHT)
        self.__configureEmotionText()
        self.__configureIntensityText()

    def __configureEmotionText(self):
        """Configure the emotion description."""
        frame = tk.Frame(self.__frame)
        frame.place(rely=self.FRAME_RELY)
        frame.place(relx=self.FRAME_RELX_E)
        frame.place(relwidth=self.FRAME_W)
        frame.place(relheight=self.FRAME_TEXT_H)
        self.__emotionText = tk.Label(frame)
        self.__emotionText.grid(row=0, column=0)
        self.__emotionText.configure(font=self.__font)

    def __configureIntensityText(self):
        """Configure the intensity description."""
        frame = tk.Frame(self.__frame)
        frame.place(rely=self.FRAME_RELY)
        frame.place(relx=self.FRAME_RELX_I)
        frame.place(relwidth=self.FRAME_W)
        frame.place(relheight=self.FRAME_TEXT_H)
        self.__intensityText = tk.Label(frame)
        self.__intensityText.grid(row=0, column=0)
        self.__intensityText.configure(font=self.__font)

    def __emodicons(self):
        """Configure the emodicons."""
        self.__configureEmotionIcon()
        self.__configureIntensityIcon()

    def __configureEmotionIcon(self):
        """Configure the emotion emodicons."""
        frame = tk.Frame(self.__frame)
        frame.place(rely=self.FRAME_RELY+self.FRAME_TEXT_H)
        frame.place(relx=self.FRAME_RELX_E)
        frame.place(relwidth=self.FRAME_W)
        frame.place(relheight=self.FULL_H-self.FRAME_TEXT_H)
        self.__emotionIcon = tk.Label(frame)
        self.__emotionIcon.grid(row=0, column=0)
        self.__emotionIcon.configure(anchor=tk.CENTER)

    def __configureIntensityIcon(self):
        """Configure the intensity emodicons."""
        frame = tk.Frame(self.__frame)
        frame.place(rely=self.FRAME_RELY+self.FRAME_TEXT_H)
        frame.place(relx=self.FRAME_RELX_I)
        frame.place(relwidth=self.FRAME_W)
        frame.place(relheight=self.FULL_H-self.FRAME_TEXT_H)
        self.__intensityIcon = tk.Label(frame)
        self.__intensityIcon.grid(row=0, column=0)
        self.__intensityIcon.configure(anchor=tk.CENTER)
