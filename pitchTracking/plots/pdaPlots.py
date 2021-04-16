import tkinter as tk                                # GUI toolkit
from matplotlib.figure import Figure                # plot element container
# canvas the figure renders into
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import perf_counter as currentTime        # API for current CPU time
from universal.constants import FRAME_PERIOD        # analysis window
from universal.constants import PROCESS_FILE        # allow user process files
from patterns.singleton import Singleton            # one instance
from patterns.switch import Switch                  # select swich
from enumerations.pdaModes import InputSources      # sound input sources
from enumerations.pdaModes import DisplayPlots  # enum for input souces
from samples.microphone import Microphone           # handle microphone
from samples.audioFile import AudioFile             # handle audio file
from processing.pitchTracker import PitchTracker    # tracking hi/lo of sound
from plots.magnitude import MagnitudePlot           # magnitude subplot
from plots.frequency import FrequencyPlot           # spectragraph subplot
from plots.pitch import PitchPlot                   # pitch subplot
from gui.sourceSwitch import SourceSwitch           # source input switch
from gui.displaySwitch import DisplaySwitch         # plot display switch


class PdaPlots(object, metaclass=Singleton):
    """Handles set of pitch detection plots."""

    TITLE = 'Pitch Detection Algorithm'             # title of form for plots
    FONTSIZE = 16                                   # font size for title
    VERTICAL_LAYOUT = True                          # stack subplot up/down
    CLEAR_TIME = 0                                  # reset elapsed time
    MIC_INTERVAL = int(FRAME_PERIOD)                # mic resampling interval
    HSPACE = 1                                      # height between subplots

    def __init__(self, win):
        """Construct object."""
        # win   window application

        self.__frame = tk.Frame(win)                # create frame from window
        self.__frame.pack(anchor=tk.CENTER)         # place center of window
        self.__frame.pack(fill=tk.BOTH)             # fill horizontal/vertical
        self.__frame.pack(expand=tk.YES)            # fill extra window space
        self.__subPlots = None                      # container for subplots
        self.__canvasWidget = None                  # object for math plots
        self.__pitchTracker = PitchTracker()        # pitch tracker instance
        self.__audioFile = AudioFile()              # audio file handler
        self.__microphone = Microphone()            # microphone handler
        self.__display = DisplaySwitch(self.__frame)    # list of plot types
        self.__elapsedTime = 0.0                    # time to track pitch
        if(PROCESS_FILE):                      # allow user select files
            self.__source = SourceSwitch(self.__frame)  # source input GUI switch

    def update(self):
        """Update the plots."""
        if(PROCESS_FILE):                      # allow user select files
            for case in Switch(self.__source.mode):
                if case(InputSources.FILE.value):
                    self.processFile()
                    break
                if case():
                    self.processMic()
        else:
            self.processMic()


    def __configPlots(self):
        if self.__canvasWidget is not None:
            self.__canvasWidget.destroy()
        self.__fig = Figure()                       # master plot element
        # title plot element
        self.__fig.suptitle(self.TITLE, fontsize=self.FONTSIZE)
        self.__numPlot = 0                          # start number of subplot
        self.__subPlots = list()                    # container for subplots
        # create mag/freq/pitch plot objects and append in container
        for case in Switch(self.__display.mode):
            if case(DisplayPlots.MAGNITUDE.value):
                self.numPlots = 1                   # number subplots display
                self.__subPlots.append(MagnitudePlot(self.__fig, self.__pos))
                break
            if case(DisplayPlots.FREQUENCY.value):
                self.numPlots = 1                   # number subplots display
                self.__subPlots.append(FrequencyPlot(self.__fig, self.__pos))
                break
            if case(DisplayPlots.PITCH.value):
                self.numPlots = 1                   # number subplots display
                self.__subPlots.append(PitchPlot(self.__fig, self.__pos))
                break
            if case(DisplayPlots.ALL.value):
                self.numPlots = 3                   # number subplots display
                self.__subPlots.append(MagnitudePlot(self.__fig, self.__pos))
                self.__subPlots.append(FrequencyPlot(self.__fig, self.__pos))
                self.__subPlots.append(PitchPlot(self.__fig, self.__pos))
                break
            if case():
                self.numPlots = 0
        # allocate more height to each subplot to make titles/x-label visable
        self.__fig.subplots_adjust(hspace=self.HSPACE)
        # utilize figure to create canvas within frame
        self.__canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
        self.__canvasWidget = self.__canvas.get_tk_widget()  # canvas widget
        self.__canvasWidget.pack(side=tk.TOP)  # place top of figure
        self.__canvasWidget.pack(fill=tk.BOTH)  # fill horizontal/vertical
        self.__canvasWidget.pack(expand=tk.YES)  # fill extra window space

    def processFile(self):
        """Update plots for audio file."""
        self.__clear()                              # clear plots past data
        self.__configPlots()                        # setup which plots to show
        self.__elapsedTime = currentTime()          # start stopwatch
        self.__audioFile.open()                     # open file for access
        if self.__audioFile.run():                  # extract data from file
            # pass data to pitch tracker
            self.__pitchTracker.data = self.__audioFile.data
            self.__update()                         # update plots w/ latest
        self.__audioFile.close()                    # close audio file
        # update display to show time to process file
        self.__updateElapsed(currentTime() - self.__elapsedTime)

    def processMic(self):
        """Update plots for microphone stream."""
        self.__clear()                              # clear plots past data
        self.__configPlots()                        # setup which plots to show
        self.__microphone.open()                    # open microphone stream
        self.__processMic()                         # start processing mic

    def __processMic(self):
        """Recursively process microphone data until mic is deselected."""
        # keep processing while mic is selected
        #if self.__source.mode == InputSources.MIC.value:
        if self.__display.mode != DisplayPlots.NONE.value:
            if self.__microphone.run():             # collect microphone data
                self.__elapsedTime = currentTime()  # start stopwatch
                # pass data to pitch tracker
                self.__pitchTracker.data = self.__microphone.data
                self.__update()  # update plots w/ latest
                # update display to show time to window of microphone data
                self.__updateElapsed(currentTime() - self.__elapsedTime)
            # periodic callback to stream data to plots
            self.__frame.master.after(self.MIC_INTERVAL, self.__processMic)
        else:
            self.__microphone.close()               # close microphone stream

    def __setElapsed(self, widget):
        """Setter for elapsed time GUI widget."""
        # widget    GUI widget for elapsed time display
        self.__elapsed = widget                     # set elapsed time widget

    """Property for setting elapsed timet."""
    elapsed = property(None, __setElapsed)

    @property
    def __pos(self):
        """Getter for location of sub-plot within form."""
        self.__numPlot = self.__numPlot + 1       # increment num sub-plot
        if self.VERTICAL_LAYOUT:                    # stack subplot up/down
            # create position string of digits for sub-plots
            pos = '{}{}{}'.format(self.numPlots, 1, self.__numPlot)
        else:                                       # stack subplot left/right
            # create position string of digits for sub-plots
            pos = '{}{}{}'.format(self.numPlots, self.__numPlot, 1)
        return int(pos)                             # integer position

    def __update(self):
        """Update sub-plots with latest data."""
        self.__pitchTracker.track()                 # track pitch from data
        for plt in self.__subPlots:                 # itterate sub-plots
            plt.update()                            # update sub-plot
        self.__canvas.draw()                        # update figure

    def __clear(self):
        """Clear plots from previous data."""
        self.__pitchTracker.clear()                 # reset pitch tracker
        self.__updateElapsed(self.CLEAR_TIME)       # clear elapsed time
        if self.__subPlots is None:
            return
        for plt in self.__subPlots:                 # itterate sub-plots
            plt.clear()                             # clear sub-plot
        self.__canvas.draw()                        # update figure

    def __updateElapsed(self, time):
        """Update elapsed time widget with new time."""
        # time  how long it took to process data

        SEC_TO_NS = 1000000000

        if self.__elapsed is not None:              # make sure widget set
            timeNs = round(time * SEC_TO_NS)        # convert sec to nanosec
            self.__elapsed.time = "{:,}".format(timeNs)       # set time
