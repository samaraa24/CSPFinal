import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import numpy as np
from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt
from model import Converter


class ConverterView(tk.Tk):
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        super().__init__()  # Use super() to call the superclass constructor
        self.title("CS Problem Solving Final Project")
        self.geometry("650x650")
        self.create_widgets()

    def setController(self, controller):
        self.controller = controller

    def uploadButtonClicked(self):
        self.controller.upload()

    def import_data(self):
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            # Process CSV data
        elif file_path.endswith((".xls", ".xlsx")):
            df = pd.read_excel(file_path)
            # Process Excel data
        elif file_path.endswith((".wav", ".mp4")):
            sample_rate, audio_data = wavfile.read(file_path)
            Converter.convert_audio(file_path, "converted_audio.wav")
            self.display_plots_and_text("converted_audio.wav")
            # Process WAV data
        else:
            # Handle other file types
            pass

    def display_plots_and_text(self, input_file):
        # Call the functions to display plots and text output
        self.plot_waveform(input_file)
        self.plot_spectrogram(input_file)
        self.display_text_output(input_file)
        self.calculate_rt60(input_file)  # Passing the input_file argument

    def plot_waveform(self, input_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        samples = np.array(audio.get_array_of_samples())
        plt.figure(figsize=(12, 8))
        plt.plot(samples)
        plt.title('Waveform Plot')
        plt.show()

    def plot_spectrogram(self, input_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        plt.figure(figsize=(8, 6))
        plt.specgram(audio.get_array_of_samples(), Fs=audio.frame_rate)
        plt.title('Spectrogram')
        plt.show()

    def calculate_rt60(self, input_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        low, mid, high = audio.dBFS - 10, audio.dBFS, audio.dBFS + 10
        rt60_low = audio.roughness(rt60_low=low)
        rt60_mid = audio.roughness(rt60_mid=mid)
        rt60_high = audio.roughness(rt60_high=high)
        rt60_difference = rt60_high - rt60_low
        plt.figure(figsize=(8, 6))
        plt.plot(rt60_low, rt60_mid, rt60_high)
        plt.title('RT60 Plot')
        plt.show()

    def display_text_output(self, input_file):
        audio = AudioSegment.from_file(input_file, format="wav")

        time_seconds = len(audio) / 1000
        max_frequency = audio.max
        rt60_low, rt60_mid, rt60_high = self.calculate_rt60(input_file)
        rt60_difference = rt60_high - rt60_low

        # Display text output using Tkinter messagebox or label, or any other widget you prefer
        text_output = f"Time in seconds: {time_seconds}\n" \
                      f"Frequency of greatest amplitude: {max_frequency} Hz\n" \
                      f"RT60 Differences in seconds: {rt60_difference}"
        messagebox.showinfo("Output", text_output)

    def create_widgets(self):
        self.import_button = tk.Button(self, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0)

    def run(self):
        self.mainloop()








