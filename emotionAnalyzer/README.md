﻿<a id="top"></a>
**Table of Contents**

1. [Goal](#Goal)
1. [Install](#Install)
    1. [Resources](##Resources)
    1. [Access](##Access)
1. [Operation](#Operation)
1. [Code](#Code)
1. [Future](#Future)

----
# Goal
> Perform real time speech analysis and emotion detection.  The application displays various audio plots and detected emotion.  Recordings are stored, while real time analysis is running.

![][gui]

[top](#top)

----
# Install

## Resources
The application is currently just Python code.  Here is a list of resources needed to run it.
1. Git
    1. Windows: Download [GitHub Desktop](https://desktop.github.com/)
    1. Linux: Perform [correct install](https://git-scm.com/download/linux) for your variant.
1. [Python](https://www.python.org/downloads/)
1. [wheel](https://pypi.org/project/wheel/)
1. [pyaudio](https://pypi.org/project/PyAudio/)
    1. Windows: 
        1. Visual Studio C++ 14.0 is required to compile the library on Windows.  Download the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools).
        1. Download the [PyAudio bindings for you version of Python](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) (e.g. PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl for Python 3.7).
        1. Install (e.g. pip3 install .\PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl).
1. [numpy](https://numpy.org/install)
1. [pillow](https://pillow.readthedocs.io/en/stable/installation.html)
1. [sklearn version 0.22.0](https://pypi.org/project/scikit-learn/0.22.2/)
    1. Windows: Change the [LongPathsEnable to 1](https://stackoverflow.com/a/62196666/9560214) or to avoid path error.
1. [soundfile](https://pypi.org/project/SoundFile/)
1. [librosa](https://pypi.org/project/librosa/)
1. [text2emotion](https://pypi.org/project/text2emotion/)
1. [matplotlib](https://pypi.org/project/matplotlib/)
1. [amfm_decompy](https://pypi.org/project/AMFM-decompy/)

## Access
The project is currently in the [vkepuska/ece5560-spring2021](https://github.com/vkepuska/ece5560-spring2021) repository.  To gain access, contact [Dr.Kepuska](<mailto:vkepuska@fit.edu>) with your GitHub username.  He will have to [invite you as a collaborator](https://github.com/vkepuska/ece5560-spring2021/settings/access) so that you can clone it.

![][collaborator]

[top](#top)

----
# Operation


[top](#top)

----
# Code
The code has been well documented.  The following shows a mapping to the various classes to GUI and processing.

[top](#top)

----
# Future
The following is a list of possible future improvements.

1. Improve Neural Network Model
    1. 
    1. 

1. Integrate Mobile Phone Solution
    1. 

1. Lie Detection
    1.

1. Quefrency
    1. 

[top](#top)
----

<!-- References -->
[teacher]: <mailto:vkepuska@fit.edu>
[gui]: image/gui.gif
[python]: https://www.python.org/downloads/release/python-3710/
[collaborator]: image/collaborator.gif