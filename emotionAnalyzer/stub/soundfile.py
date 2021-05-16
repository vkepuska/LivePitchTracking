class SoundFile(object):
  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    pass

  def __init__(self, fileName):
    self.__samplerate = 0

  def open(self):
    pass

  def read(self, dtype):
    return 0

  @property
  def samplerate(self):
      return self.__samplerate
