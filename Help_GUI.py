from tkinter import *
from functools import partial

import random

class Quiz:
    def __init__(self, parent):

        # variable formatting
        background_colour = "lavender"

        # Quiz Main screen GUI
        self.quiz_frame = Frame(width=640, height=480, bg=background_colour,
                                pady=10)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_label = Label(self.quiz_frame, text="         My Quiz           ",
                                          font=("Ubuntu", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help",
                                  font=("Ubuntu", "16", "bold"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Help:
    def __init__(self, partner):
        background = "bisque"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background,
                                pady=10)
        self.help_frame.grid()

        # Set up 'Help' heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="ubuntu 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="Instructions",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="ghost white", font="ubuntu 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("My Quiz")
    something = Quiz(root)
    root.mainloop()