from plots.subplot import SubPlot                   # parent class for subplot


class PitchPlot(SubPlot):
    """Handles pitch tracking plots."""

    # Constants
    TITLE = 'Pitch'                                 # title of plot
    XLABEL = 'Samples'                              # label for x-axis
    YLABEL = 'Pitch Magnitude'                      # label for y-axis
    Y_BOTTOM = 0                                    # bottom range at 0 Hz
    Y_TOP = 300                                     # top range at 300 Hz
    PITCH_LABEL = 'pitch interpolation'             # label text non-interp
    PITCH_COLOR = 'green'                           # plot color non-interp
    STEP_LABEL = 'step interpolation'               # label text step-interp
    STEP_COLOR = 'blue'                             # plot color setp-interp
    SPLINE_LABEL = 'spline interpolation'           # label text spline-interp
    SPLINE_COLOR = 'red'                            # plot color spline-interp
    LEGEND = 'upper right'                          # location for ledgend
    SHOW_GRID = True                                # show grid lines in plot

    def update(self):
        """Updates plot with latest data."""
        self.clear()                                # clear previous data
        self.__plot()                               # plot data
        self._plt.legend(loc=self.LEGEND)           # reset ledgend
        self._plt.grid(self.SHOW_GRID)              # show grid
        self._plt.axes.set_xlim(left=0)             # start at 0th sample
        self._plt.axes.set_xlim(right=self._pitchTracker.length)    # end point
        self._plt.axes.set_ylim(bottom=self.Y_BOTTOM)  # y-axis lower range
        self._plt.axes.set_ylim(top=self.Y_TOP)     # y-axis upper range
        self._labelRefresh()                        # refresh labels

    def __plot(self):
        """Plot the different types of pitch data."""
        self._plt.plot(self._pitchTracker.pitch,    # non-interp pitch samples
                       label=self.PITCH_LABEL,      # non-interp label text
                       color=self.PITCH_COLOR)      # non-interp plot color
        self._plt.plot(self._pitchTracker.step,     # step-interp pitch samples
                       label=self.STEP_LABEL,       # step-interp label text
                       color=self.STEP_COLOR)       # step-interp plot color
        self._plt.plot(self._pitchTracker.spline,   # spline-intrp pitch sampls
                       label=self.SPLINE_LABEL,     # spline-interp label text
                       color=self.SPLINE_COLOR)     # spline-interp plot color
