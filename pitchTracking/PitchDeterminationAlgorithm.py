"""
Real-time or file based pitch analysis.

File: PitchDeterminationAlgorithm.py
Author: Richard Hemphill
ID: 903877709
Class: ECE5550 High Performance Computing
Teacher: Dr. Veton Kepuska
Project: Perform sound analysis with ability to utilize GPU or CPU for
    processing. There are 3 plots (magnitude, frequency, pitch).  The data
    comes from either sound file or microphone.  The window provides a GUI with
    command buttons for easier control.  An elapsed time is displayed for the
    user to demonstrate GPU vs CPU performance.
"""

from gui.window import PDA      # class that manages GUI for this project

# Designated Start of Program
if __name__ == '__main__':
    pda = PDA()                 # instantiate PDA object
    pda.run()                   # activate PDA object
