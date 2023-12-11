import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt
from model import Converter
from controller import Controller


class ConverterView(tk.Tk):
    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        self.window = tk.Tk()
        self.window.title("CS Problem Solving Final Project")
        self.window.geometry("650x650")
        self.create_widgets()

    def setController(self, controller):
        self.controller = controller

    def uploadButtonCLicked(self):
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
            converter_view_instance = ConverterView(controller, model)
            # Call the display_plots_and_text method on the instance
            converter_view_instance.display_plots_and_text("converted_audio.wav")

            # Process WAV data

        else:
            # Handle other file types
            pass

        # ...

        def display_plots_and_text(self, converted_file_path):
            # Call the functions to display plots and text output
            self.plot_waveform(converted_file_path)
            self.plot_spectrogram(converted_file_path)
            self.calculate_rt60(converted_file_path)  # Passing the input_file argument
            self.display_text_output(converted_file_path)

    # ...

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

    def plot_rt60(self, input_file):
        audio = AudioSegment.from_file(input_file, format="wav")
        rt60_low, rt60_mid, rt60_high = calculate_rt60(input_file)
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
        messagebox.showinfo(title="Greetings", message="Hello World")

    def create_widgets(self):
        self.import_button = tk.Button(self.controller, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0)

    def run(self):
        self.window.mainloop()






