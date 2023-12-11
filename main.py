
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from view import ConverterView
from model import Converter


def __init__(self, master):
  self.master = master
  self.master.title("Data Analysis and Modeling Platform")
  self.create_widgets()

def main():
  root = tk.Tk()
  converter_model = Converter()
  app = ConverterView(root, converter_model)
  root.mainloop()

if __name__ == "__main__":
  main()

def clean_data(self):
  pass

def analyze_data(self):
  pass

def model_data(self):
  pass

def generate_report(self):
  pass

