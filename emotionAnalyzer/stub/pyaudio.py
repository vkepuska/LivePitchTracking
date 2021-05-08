paInt16 = None

class PyAudio(object):
  def __init__(self):
    self.__stream = Stream()
    pass

  def open(self):
    return self.__stream

class Stream(object):
  def __init__(self):
    pass

  def start_stream(self):
    pass

  def read(self):
    pass

  def stop_stream(self):
    pass