from tkinter import *
from functools import partial   # to make sure there aren't any unwanted windows

import random

class Quiz:
    def __init__(self):

        # variable formatting
        background_colour = "#84e8bb"

        # Main Screen Frame
        self.quiz_frame = Frame(bg=background_colour,
                                pady=10)
        self.quiz_frame.grid()

    # Quiz Heading (row 0)
    self.quiz_heading_label = Label(self.quiz_frame,
                                    text="test",
                                    font="Ubuntu 18 Bold",
                                    bg=background_colour,
                                    padx=10, pady=10)
    self.quiz_heading_label.grid(row=0)

    #

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("My Quiz")
    something = Quiz(root)
    root.mainloop()