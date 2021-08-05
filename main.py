import tkinter as tk
from tkinter import ttk

import warnings
warnings.filterwarnings("ignore")

from gui.xgboost import XGBoost

class GUI:
    def __init__(self):
        self.gui = tk.Tk()
        self.parent = ttk.Notebook(self.gui)
      
        xgboost = XGBoost()
        self.add(xgboost, "XGBoost")

        self.parent.pack(expand=1, fill='both')

    def add(self, frame, text):
        self.parent.add(frame.root, text=text)

    def start(self):
        self.gui.mainloop()

s = GUI()
s.start()
