from scipy.io import wavfile 
import scipy.io

#opens a wav file 
scipy.io.wavfile.read(clap.m4a, mmap = False)

#display name of file
clap = 'clap.wav' 
samplerate, data = wavefile.read(clap)
print(f"the number of channels = {data.shape[len(data.shape) - 1]}")
print(f"sample rate = {samplerate}Hz")
length = data.shape[0] / samplerate
print(f"length = {length}s")
