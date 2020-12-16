from tkinter import *

root = Tk()
root.title("Make your bet!  ")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 20, padx = 60)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { "red", "orange", "yellow", "green", "blue", "purple" }
tkvar.set('red') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a color").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
