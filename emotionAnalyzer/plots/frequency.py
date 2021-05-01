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
    VMIN = -1E0                                     # min value for color scale
    VMAX = 1E2                                      # max value for color scale
    SCALE = 'dB'                                    # linear or dB
    MODE = 'magnitude'                              # psd, magnitude, angle, phase

    def update(self):
        """Updates plot with latest data."""
        self._plt.specgram(self._pitchTracker.data,         # signal to plot
                           window=window_hanning,   # tapering window to used
                           Fs=FS,                   # sampling frequency use
                           NFFT=self.NTTF,          # num of FFT points used
                           noverlap=self.OVERLAP_LENGTH,    # amount overlap
                           cmap=self.COLOR_MAP,     # type of colors
                           vmin=self.VMIN,          # white
                           vmax=self.VMAX,          # black
                           scale=self.SCALE,        # scale the energy
                           mode=self.MODE)          # spectrum to use
        self._labelRefresh()                        # reapply labels
