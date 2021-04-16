import amfm_decompy.pYAAPT as pYAAPT                # pitch tracking algorithm
import amfm_decompy.basic_tools as basic            # pitch tracking utilities
from patterns.singleton import Singleton            # design pattern (one inst)
from universal.constants import FS                  # sampling frequency


class PitchTracker(object, metaclass=Singleton):
    """Handles pitch processing."""

    def __init__(self):
        """Construct object."""
        self.__rate = FS                            # sampling frequency
        self.__data = None                          # sample data to process
        self.__pitch = None                         # pitch track (raw)
        self.__step = None                          # step interpolated pitch
        self.__spline = None                        # spline interpolate pitch
        self.__length = 0                           # number of points

    def track(self):
        """Track pitch."""
        self.__track()                              # track pitch

    def clear(self):
        """Clear data."""
        self.__data = None

    @property
    def data(self):
        """Returns sample data."""
        return self.__data

    @data.setter
    def data(self, values):
        """Sets the data with sample values."""
        # values    sample values

        self.__data = values

    @property
    def pitch(self):
        """Returns non-interpolated pitch."""
        return self.__pitch

    @property
    def step(self):
        """Returns step-interpolated pitch."""
        return self.__step

    @property
    def spline(self):
        """Returns spline-interpolated pitch."""
        return self.__spline

    @property
    def length(self):
        """Returns number of pitch points."""
        return self.__length

    def __track(self):
        """Process pitch tracks."""
        s = basic.SignalObj(self.__data, self.__rate)   # basic signal object
        pitch = pYAAPT.yaapt(s)                         # pitch object

        self.__pitch = pitch.values                 # no-inerpolation pitch

        pitch.set_values(pitch.samp_values, len(pitch.values),
                         interp_tech='step')        # apply interpolation
        self.__step = pitch.values                  # store step interpol val

        pitch.set_values(pitch.samp_values, len(pitch.values),
                         interp_tech='spline')      # apply interpolation
        self.__spline = pitch.values                # store spline interpol val

        self.__length = len(self.__pitch)           # number of points in pitch
