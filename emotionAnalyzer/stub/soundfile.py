class SoundFile(object):
  def __enter__(self):
        return self

  def __init__(self, fileName):
    self.__samplerate = 0

  def open(self):
    pass

  @property
  def samplerate(self):
      return self.__samplerate
