from processing.pitchTracker import PitchTracker    # tracking hi/lo of sound


class SubPlot(object):
    """Parent class for sub-plots."""

    # Constants
    TITLE_SIZE = 12                                 # font size for title
    LABEL_SIZE = 10                                 # font size for labels
    ENABLE = True                                   # activate autoscaling
    AXIS = 'y'                                      # auto scale to y-axis only
    TIGHT = True                                    # keep signal peak in plot

    def __init__(self, fig, pos):
        """Constructs object."""
        # fig   figure widget
        # pos   position to place the sub-plot

        self._plt = fig.add_subplot(pos)            # add subplot to figure
        self._labelInit()                           # initialize labels
        self._pitchTracker = PitchTracker()         # PitchTracker instance

    def clear(self):
        """Clear data from sub-plot."""
        self._plt.clear()

    def _labelInit(self):
        """Initialize text and font size of sub-plot title/label."""
        # title above sub-plot
        self._plt.set_title(self.TITLE, fontsize=self.TITLE_SIZE)
        # label of x-axis data
        self._plt.set_xlabel(self.XLABEL, fontsize=self.LABEL_SIZE)
        # label of y-axis data
        self._plt.set_ylabel(self.YLABEL, fontsize=self.LABEL_SIZE)

    def _labelRefresh(self):
        """Reapply sub-plot title/label text since it disappers on clear."""
        self._plt.set_title(self.TITLE)             # title above sub-plot
        self._plt.set_xlabel(self.XLABEL)           # label of x-axis data
        self._plt.set_ylabel(self.YLABEL)           # label of y-axis data
