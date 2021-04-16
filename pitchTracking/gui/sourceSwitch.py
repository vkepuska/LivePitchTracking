from enumerations.pdaModes import InputSources      # enum for input souces
from gui.commandSwitches import CommandSwitch       # parent for toggle switch


class SourceSwitch(CommandSwitch):
    """Class for toggling between source for auditory data."""

    # Constants
    COLOR = 'red'                                   # color of toggle switch

    def __init__(self, form):
        """Construct object."""
        # form  container form that switch will embed in

        self.__modes = InputSources                 # enum of switch modes
        # call parent constructor
        super().__init__(form=form, modes=self.__modes, color=self.COLOR)

    def __setPlots(self, plots):
        """Set plot objects."""
        # plots widget with callbacks to used when button is pressed

        # assign callbacks to enums
        self.buttons[InputSources.FILE.name].config(command=plots.update)
        self.buttons[InputSources.MIC.name].config(command=plots.update)

    """Property for setting plots widget."""
    plots = property(None, __setPlots)
