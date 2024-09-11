import tkinter as tk
from tkinter import ttk


# Class for Frame Widget
class BaseFrame(ttk.Frame):
    def __init__(self, parent, width, height, x, y):
        super().__init__(parent, width=width, height=height, borderwidth=10, relief=tk.GROOVE)
        self.place(x=x, y=y)


# Class for ttk.Button Widget
class ButtonWidget(ttk.Button):
    def __init__(self, parent, text, command, style, x, y):
        super().__init__(parent, text=text, command=command, style=style)
        self.place(x=x, y=y)


# Class for Entry Widget
class EntryWidget(tk.Entry):
    def __init__(self, parent,pos, **kwargs):
        super().__init__(parent, **kwargs)
        self.place(x=pos[0], y=pos[1])

    # Get the value from the user
    def return_value(self):
        return self.get()

    # Deleting entry
    def clear(self):
        self.delete(0, tk.END)


# Class for Label Widget
class LabelWidget(ttk.Label):
    def __init__(self, parent, text, font, pos):
        super().__init__(parent, text=text, font=font)
        self.place(x=pos[0], y=pos[1])


# Class for tk.Button Widget
class OrdinaryButtonWidget(tk.Button):
    def __init__(self, parent, text, command, font, padx, x, y):
        super().__init__(parent, text=text, command=command, font=font, padx=padx)
        self.place(x=x, y=y)
