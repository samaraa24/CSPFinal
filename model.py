import os, io
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
# import sox as sox

class Converter:

  @staticmethod
  def convert_audio(src, dist):
    sound = AudioSegment.from_mp3(src)
    sound.export(dist, format="wav")
    raw_audio = AudioSegment.from_file(dist, format="wav")
    channel_count = raw_audio.channels
    print(f"Channel count before conversion: {channel_count}")
    mono_wav = raw_audio.set_channels(1)
    mono_wav.export("pt_mono.wav", format="wav")
    mono_wav_audio = AudioSegment.from_file("pt_mono.wav", format="wav")
    channel_count = mono_wav_audio.channels
    print(f"Channel count after conversion: {channel_count}")
    return os.path.abspath("pt_mono.wav")


def remove_metadata(input_file):
  audio = AudioSegment.from_file(input_file, format="mp4")
  if audio.info.tags:
      audio = audio.clear()
  return audio

def plot_waveform(input_file):
  audio = AudioSegment.from_file(input_file, format="mp4")
  samples = np.array(audio.get_array_of_samples())

  plt.figure(figsize=(12, 8))

  for i in range(1, 7):
      plt.subplot(2, 3, i)
      plt.plot(samples)
      plt.title(f'Waveform Plot {i}')

  plt.show()

def calculate_rt60(input_file):
  audio = AudioSegment.from_file(input_file, format="mp4")
  low, mid, high = audio.dBFS - 10, audio.dBFS, audio.dBFS + 10
  rt60_low = audio.roughness(rt60_low=low)
  rt60_mid = audio.roughness(rt60_mid=mid)
  rt60_high = audio.roughness(rt60_high=high)
  return rt60_low, rt60_mid, rt60_high

def plot_spectrogram(input_file):
  audio = AudioSegment.from_file(input_file, format="mp4")
  plt.figure(figsize=(8, 6))
  plt.specgram(audio.get_array_of_samples(), Fs=audio.frame_rate)
  plt.title('Spectrogram')
  plt.show()

def text_output(input_file):
  audio = AudioSegment.from_file(input_file, format="mp4")

  time_seconds = len(audio) / 1000
  max_frequency = audio.max
  rt60_low, rt60_mid, rt60_high = calculate_rt60(input_file)
  rt60_difference = rt60_high - rt60_low

  print(f"Time in seconds: {time_seconds}")
  print(f"Frequency of greatest amplitude: {max_frequency} Hz")
  print(f"RT60 Differences in seconds: {rt60_difference}")
