import tkinter as tk                                # GUI toolkit
from tkinter import Canvas
import tkinter.font as font                         # font parameters
from PIL import ImageTk
from PIL import Image
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
    DEFAULT_EMOTION = 0                         # emotion to load at start
    DEFAULT_INTENSITY = 0                       # intensity to load at start

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

    def __insert(self,container,icon):
        """Insert images into container"""
        img = Image.open(self.FOLDER+icon.name+self.EXTENSION)
        resizedImg = img.resize((240, 240), Image.ANTIALIAS)
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
        self.__font = font.Font(family=self.FONT_FAMILY,
                                size=self.FONT_SIZE, weight=self.FONT_WEIGHT)
        self.__emotionTextFrame = tk.Frame(self.__frame)
        self.__emotionTextFrame.place(relx=0.0)
        self.__emotionTextFrame.place(rely=0.0)
        self.__emotionTextFrame.place(relwidth=0.5)
        self.__emotionTextFrame.place(relheight=0.1)
        self.__emotionText = tk.Label(
            self.__emotionTextFrame, text='Emotion')
        self.__emotionText.grid(row=0, column=0)
        self.__emotionText.configure(font=self.__font)

        self.__intensityTextFrame = tk.Frame(self.__frame)
        self.__intensityTextFrame.place(relx=0.5)
        self.__intensityTextFrame.place(rely=0.0)
        self.__intensityTextFrame.place(relwidth=0.5)
        self.__intensityTextFrame.place(relheight=0.1)
        self.__intensityText = tk.Label(
            self.__intensityTextFrame, text='Intensity')
        self.__intensityText.grid(row=0, column=0)
        self.__intensityText.configure(font=self.__font)

    def __emodicons(self):
        self.__emotionIconFrame = tk.Frame(self.__frame)
        self.__emotionIconFrame.place(relx=0.0)
        self.__emotionIconFrame.place(rely=0.1)
        self.__emotionIconFrame.place(relwidth=0.5)
        self.__emotionIconFrame.place(relheight=1.0)
        self.__emotionIcon = tk.Label(self.__emotionIconFrame, image=self.__emotion[self.DEFAULT_EMOTION])
        self.__emotionIcon.grid(row=0, column=0)
        self.__emotionIcon.configure(anchor=tk.CENTER)

        self.__intensityIconFrame = tk.Frame(self.__frame)
        self.__intensityIconFrame.place(relx=0.5)
        self.__intensityIconFrame.place(rely=0.1)
        self.__intensityIconFrame.place(relwidth=0.5)
        self.__intensityIconFrame.place(relheight=1.0)
        self.__intensityIcon = tk.Label(self.__intensityIconFrame, image=self.__intensity[self.DEFAULT_INTENSITY])
        self.__intensityIcon.grid(row=0, column=0)
        self.__intensityIcon.configure(anchor=tk.CENTER)
