from tkinter import *
from functools import partial   # to make sure there aren't any unwanted windows

import random

class Quiz:
    def __init__(self, parent):


        # variable formatting
        background_colour = "#84e8bb"


        # Main Screen Frame
        self.quiz_frame = Frame(width=640, height=480, bg=background_colour,
                                pady=10)
        self.quiz_frame.grid()


        # Quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text="test",
                                        font="Ubuntu 18 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)


        # User Instructions (row 1)
        self.quiz_instructions_label = Label(self.quiz_frame,
                                             text="Welcome to my quiz! "
                                             "Click start to begin!",
                                             font="Ubuntu 10 italic", wrap=300,
                                             justify=LEFT, bg=background_colour,
                                             padx=10, pady=10)
        self.quiz_instructions_label.grid(row=1)

        # Start button (row 2)

        # Answer entry box (row 3)
        self.quiz_answer_entry = Entry(self.quiz_frame, width=20,
                                      font="Ubuntu 14 bold")
        self.quiz_answer_entry.grid(row=3)

        # History / Export Button frame (row 4)
        self.export_hist_frame = Frame(self.quiz_frame)
        self.export_hist_frame.grid(row=5, pady=10)

        self.quiz_hist_button = Button(self.export_hist_frame, font="Ubuntu 12 bold",
                                       text="Question History", width=15, bg="cadet blue")
        self.quiz_hist_button.grid(row=0, column=0)

        self.export_button = Button(self.export_hist_frame, font="Ubuntu 12 bold",
                                    text="Help", width=5, bg="dark grey")
        self.export_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("My Quiz")
    something = Quiz(root)
    root.mainloop()