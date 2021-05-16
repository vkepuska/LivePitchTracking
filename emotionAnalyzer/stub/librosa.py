import numpy as np

def stft(value):
  return 0

class feature:
  @classmethod
  def mfcc(cls, y, sr, n_mfcc):
    return np.zeros(1)
  
  @classmethod
  def chroma_stft(cls, yS, sr, n_mfcc):
    return np.zeros(1)

  @classmethod
  def melspectrogram(cls, y, sr):
    return np.zeros(1)

  @classmethod
  def spectral_contrast(cls, S, sr):
    return np.zeros(1)

  @classmethod
  def tonnetz(cls, y, sr):
    return np.zeros(1)

class effects:
  @classmethod
  def harmonic(cls, y):
    return np.zeros(1)
