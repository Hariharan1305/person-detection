# Import module from tkinter for UI:
from tkinter import *
import os

# Creating instance of TK:
root = Tk()
root.configure(background="yellow")


# Function for detection:
def function1():
    os.system("py bike_detection.py")


def function2():
    os.system("py person_detection.py")


def function3():
    os.system("py car_detection.py")


def function4():
    os.system("py bus.py")


def function6():
    root.destroy()


# Title for the window:
root.title("Vehicle and Person detection")

# Creating a text label for window:
Label(root, text="Vehicle and Person detection", font=("Lucida Console", 20), fg="white",
      bg="red", height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Bike Detection", font=("Lucida Console", 20), bg="white", fg='red', command=function1).grid(row=4,
                                                                                                                columnspan=2,
                                                                                                                sticky=W + E + N + S,
                                                                                                                padx=5,
                                                                                                                pady=5)

# creating second button
Button(root, text="Person Detection", font=("Lucida Console", 20), bg="white", fg='red', command=function2).grid(row=5,
                                                                                                                  columnspan=2,
                                                                                                                  sticky=N + E + W + S,
                                                                                                                  padx=5,
                                                                                                                  pady=5)

# creating third button
Button(root, text="Car Detection", font=('Lucida Console', 20), bg="white", fg="red", command=function3).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

Button(root, text="Bus Detection", font=('Lucida Console', 20), bg="white", fg="red", command=function4).grid(row=7,
                                                                                                                 columnspan=2,
                                                                                                                 sticky=N + E + W + S,
                                                                                                                 padx=5,
                                                                                                                 pady=5)

Button(root, text="Exit", font=('Lucida Console', 20), bg="white", fg="red", command=function6).grid(row=9,
                                                                                                      columnspan=2,
                                                                                                      sticky=N + E + W + S,
                                                                                                      padx=5, pady=5)

root.mainloop()
