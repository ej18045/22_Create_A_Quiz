from tkinter import *
from functools import partial  # to make sure there aren't any unnecessary windows
# to prevent unwanted windows

import random

class Quiz:
    def __init__(self, parentX):
        # Formatting Variables
        self.history = None
        background_colour = "#0097a7"
        
        # In actual program this is blank and is populated with user calculations
        self.all_ans_list = ['Question 1 is incorrect',
                             'Question 2 is correct',
                             'Question 3 is correct',
                             'Question 4 is incorrect',
                             'Question 5 is correct',
                             'Question 6 is incorrect',
                             'Question 7 is incorrect',
                             'Question 8 is incorrect',
                             'Question 9 is incorrect',
                             'Question 10 is correct']
        
        # Quiz Main Screen GUI
        self.quiz_frame = Frame(width=640, height=480, bg=background_colour,
                                pady=10)
        self.quiz_frame.grid()
        
        # Quiz Heading (row 0)
        self.quiz_label = Label(self.quiz_frame, text="         My Quiz           ",
                                          font=("Ubuntu", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.quiz_frame, text="History",
                                  font=("Ubuntu", "14"),
                                  padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

        def history(self):
                        get_history = history(self)
                        get_history.history_text.configure(text="History text goes here")


class history:
    def __init__(self, partner):
        background = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background,
                                   pady=10)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="history / Instructions",
                                 font="ubuntu 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent quiz"
                                       "answers. Please use the"
                                       "export button to create a text"
                                       "file of all your answers for"
                                       "this session", wrap=250,
                                  font="ubuntu 10 italic",
                                  justify=LEFT, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here... (row 2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Ubuntu 12 bold")
        self.export_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("My Quiz")
    something = Quiz()
    root.mainloop()
