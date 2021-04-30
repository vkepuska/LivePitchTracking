"""
File: SpeechEmotionAnalyzer.py
Author: Richard Hemphill
Class: ECE5560 Computer Systems
Teacher: Dr. Veton Kepuska
Project: Perform speech analysis with ability to detect emotions.
"""

# class that manages GUI for this project
from gui.window import SEA

# Designated Start of Program
if __name__ == '__main__':
    sea = SEA()     # instantiate GUI
    sea.run()       # activate GUI