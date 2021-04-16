from enumerations.pdaModes import DisplayPlots      # enum for input souces
from gui.commandSwitches import CommandSwitch       # parent for toggle switch


class DisplaySwitch(CommandSwitch):
    """Class for toggling processor to handle calculations."""

    COLOR = 'blue'                                  # color of toggle switch

    def __init__(self, form):
        """Construct object."""
        # form  container form that switch will embed in

        self.__modes = DisplayPlots                 # enum of switch modes
        # call parent constructor
        super().__init__(form=form, modes=self.__modes, color=self.COLOR)

    def __setPlots(self, plots):
        """Set plot objects."""
        # plots widget with callbacks to used when button is pressed

        # assign callbacks to enums
        self.buttons[DisplayPlots.NONE.name].config(command=plots.update)
        self.buttons[DisplayPlots.MAGNITUDE.name].config(command=plots.update)
        self.buttons[DisplayPlots.FREQUENCY.name].config(command=plots.update)
        self.buttons[DisplayPlots.PITCH.name].config(command=plots.update)
        self.buttons[DisplayPlots.ALL.name].config(command=plots.update)

    """Property for setting plots widget."""
    plots = property(None, __setPlots)
