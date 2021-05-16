def stft(value):
  return 0

class feature:
  @classmethod
  def mfcc(cls, y):
    return 0
  
  @classmethod
  def chroma_stft(cls, y, sr, n_mfcc):
    return 0

  @classmethod
  def melspectrogram(cls, y, sr):
    return 0

  @classmethod
  def spectral_contrast(cls, S, sr):
    return 0

  @classmethod
  def tonnetz(cls, y, sr):
    return 0


class effects:
  @classmethod
  def harmonic(cls, y):
    return 0
