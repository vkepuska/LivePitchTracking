# pitch
> Perform sound analysis with ability to utilize GPU or CPU for processing. There are 3 plots (magnitude, frequency, pitch).  The data comes from either sound file or microphone.  The window provides a GUI with command buttons for easier control.  An elapsed time is displayed for the user to demonstrate GPU vs CPU performance.

![][gui]
----
**Table of Contents**
<!--ts-->
1. [Install](#Install)
1. [Run](#Run)
1. [Code](#Code)
1. [Analysis](#Analysis)
1. [Meta](#Meta)
<!--te-->

----
## Meta

**School:** [Florida Institute of Technology][fit]

**Class:** [ECE5550 High Performance Computing][class]

**Author:** [Richard Hemphill][author]

**Teacher:** [Dr. Veton Kepuska][teacher]

**Semester:** Spring 2020

**Repo:** [https://github.com/vkepuska/pitch]

----
## Install
### Pitch
1. Open terminal.
1. Clone [pitch repository][pitch-repo].
```
> git clone https://github.com/vkepuska/pitch
```
### AMFM_decompy_cuda
1. Open terminal.
1. Clone [AMFM_decompy_cuda repository][track-cuda-repo].
```
> git clone https://github.com/bjbschmitt/AMFM_decompy
```
3. Navigate to AMFM_decompy_cuda folder.
4. Run setup.
```
> python ./setup.py install
```
### Other Modules
1. When [running](#Run), there may be an error.
> ModuleNotFoundError: No module named 'tbd'
1. Install any missing modules from your environment.
1. Open terman as administrator.
   1. Type *'cmd'* in search bar.
   1. Click on *'Run as administrator.'*
```
> pip install tbd
```
----
## Run
### Terminal
1. Change directory to location of [pitch repository][pitch-repo].
1. Open with Python.
```
> python ./PitchDeterminationAlgorithm.py
```
----
## Code
The code has been well documented.  The following shows a mapping to the various classes.
![][map]

----
## Analysis

Refactored [AMFM Decompy Cuda][track-cuda-repo] to use [cupy][cupy] calls [equivalent][compare] to [numpy][numpy].  Switching between CPU and GPU showed a reduction in speed for the GPU.  The following table shows the processing time in nano-seconds.
[File][ngs-zip]|CPU|GPU
---|---:|---:
ENG_F.wav|765,168,400|1,034,716,400
ENG_F.wav|978,630,000|991,998,100
english.wav|709,859,500|716,154,100
1nw0000pes.wav|4,130,238,700|4,094,621,100
f1nw0000pes_short.wav|406,263,900|423,472,600
female.wav|2,957,754,500|3,145,098,500
m1nw0000pes_short.wav|505,823,100|509,783,700
male.wav|2,962,983,300|3,105,702,900

Theory is that there is too much overhead moving data between host (CPU) and devide (GPU). The following analyze the various calls with increasing buffer size.

### Zeros
Used [numpy][numpy] and [cupy][cupy] to create a buffer of [zeros][cupy-zeros].  As shown below, there is no benefit in just using the GPU to create the zeros.

![][plot-zeros]

### Buffer Shifting
Used [numpy][numpy] and [cupy][cupy] to create a buffer of [random numbers][cupy-random].  As shown below, there are benefits if the data is large enough, but moving the data back into the host has an overhead that removes the benefit.

![][plot-buffShift]

----
## Conclusion
Utilizing the GPU has benefits for large data sets that are mostly kept in the device.  Therefore, it is not recommended for pitch tracking.


----
<!-- Image Reference -->
[fit]: https://www.fit.edu/
[class]: http://my.fit.edu/~vkepuska/web/courses.php#ece5550-files
[author]: (mailto:rhemphill2019@my.fit.edu)
[teacher]: <mailto:vkepuska@fit.edu>
[pitch-repo]: https://github.com/vkepuska/pitch
[track-cuda-repo]: https://github.com/richardhemphill/AMFM_decompy_cuda
[track-repo]: https://github.com/bjbschmitt/AMFM_decompy
[gui]: image/gui.gif
[map]: image/classMap.gif
[plot-zeros]: image/zeros.png
[plot-buffShift]: image/buffer_shift.png
[numpy]: https://docs.scipy.org/doc/numpy/reference/index.html#reference
[cupy]: https://docs-cupy.chainer.org/en/stable/reference/
[compare]: https://docs-cupy.chainer.org/en/stable/reference/comparison.html
[cupy-zeros]: https://docs-cupy.chainer.org/en/stable/reference/generated/cupy.zeros.html#cupy.zeros
[cupy-random]: https://docs-cupy.chainer.org/en/stable/reference/generated/cupy.random.random.html
[ngs-zip]: http://my.fit.edu/~vkepuska/ece5550/Corpora/