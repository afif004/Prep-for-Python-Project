#basic window with widgets
'''
Widgets are building blocks of Tkinter
i.e. texts,buttons,menus,frames etc.
Understanding the widgets and controlling them is key to mastering any GUI framework

TKinter has 2 sets of widgets
tk widgets were the og
ttk widgets were added later on (more modern)
'''
import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was clicked')
def print_hello():
    print('hello')

#crete window - call tk.Tk() function & its gonna return the actual 
# window in which we place everything in
window = tk.Tk()
#to display a certain variable - variable.mathod()
window.title('Window & Widgets')
#set size of window geometry('widthxheight')
window.geometry('800x500')

#ttk widgets
label = ttk.Label(master = window, text='Thi is a test')
label.pack()

#tk.text
text = tk.Text(master = window)
text.pack()
#tk.Text(master = window) only cretes the widget & tells what the parent is. Does not place it visually.
#the method .pack() takes a widget and then packs it all the way on the top center like a stack

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

text_label = ttk.Label(master = window, text='My label')
text_label.pack()

#ttk button - never call a function in command as we don't want the button to call the function without getting clicked
button = ttk.Button(master=window, text='A Button', command=button_func)
button.pack()

#exercise
#text label

#button
#button_hello = ttk.Button(master=window, text='Print Hello', command=print_hello)
button_hello = ttk.Button(master=window, text='Print Hello', command=lambda:print('hello'))
button_hello.pack()

#run
window.mainloop()
'''
mainloop - 1. Updates to GUI 
              [Wriiten text or updatation of widgets actually gets displayed]
           2. Checks for events [Button clicks, mouse movements, closing the window]
without mainloop app can't run
'''