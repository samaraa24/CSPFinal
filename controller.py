import matplotlib.pyplot as plt
import numpy as np
from model import Converter
from view import ConverterView
import tkinter as tk


class Controller():

    def __init__(self):
        self.model = model
        self.view = view

    def upload(self):
        self.model.openFile()
        self.view.filePath = self.model.getFileName()
        self.view.fileUploaded()

    def getWavLength(self):
        return self.model.getWavLength()

    def plotWave(self):
        self.model.plotWave()
        self.view.plotWave(self.model.fig)

    def run(self):
        self.view.run()


root = tk.Tk()
model = Converter()
view = ConverterView(Controller, model)
controller = Controller(model, view)
view.setController(controller)
view.grid(row=0, column=0)

root.mainloop()

if __name__ == "__main__":
    controller = Controller()
    controller.run()
