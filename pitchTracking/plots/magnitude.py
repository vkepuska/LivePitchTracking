from plots.subplot import SubPlot                   # parent class for subplot


class MagnitudePlot(SubPlot):
    """Handles spectrogram plots."""

    # Constants
    TITLE = 'Speech Waveform'                       # title of plot
    XLABEL = 'Samples'                              # label for x-axis
    YLABEL = 'Magnitude'                            # label for y-axis
    Y_BOTTOM = -20000                               # bottom range
    Y_TOP = 20000                                   # top range

    def update(self):
        """Updates plot with latest data."""
        self.clear()                                # remove signals from plot
        self._plt.plot(self._pitchTracker.data)     # plot data from source
        self._plt.axes.set_xlim(left=0)             # start at 0th sample
        self._plt.axes.set_xlim(right=self._pitchTracker.length)  # end point
        self._plt.axes.set_ylim(bottom=self.Y_BOTTOM)  # y-axis lower range
        self._plt.axes.set_ylim(top=self.Y_TOP)     # y-axis upper range
        self._labelRefresh()                        # reapply labels
