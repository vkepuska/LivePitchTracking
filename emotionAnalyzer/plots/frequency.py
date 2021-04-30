from matplotlib.mlab import window_hanning          # hann tapering window
from universal.constants import FS                  # sampling frequency
from plots.subplot import SubPlot                   # parent class for subplot


class FrequencyPlot(SubPlot):
    """Handles spectrogram plots."""

    # Constants
    TITLE = 'Spectrogram of Speech'                 # title of plot
    XLABEL = 'Time'                                 # label for x-axis
    YLABEL = 'Spectral Magnitude'                   # label for y-axis
    NTTF = 1024                                     # num of FFT points
    OVERLAP_LENGTH = 900                            # overlap between blocks
    COLOR_MAP = 'Greys'                             # color of spectrograph
    MODE = 'magnitude'                              # magnitude spectrum

    def update(self):
        """Updates plot with latest data."""
        self._plt.specgram(self._pitchTracker.data,         # signal to plot
                           window=window_hanning,   # tapering window to used
                           Fs=FS,                   # sampling frequency use
                           NFFT=self.NTTF,          # num of FFT points used
                           noverlap=self.OVERLAP_LENGTH,    # amount overlap
                           cmap=self.COLOR_MAP,
                           mode=self.MODE)          # spectrum to use
        self._labelRefresh()                        # reapply labels
