#tk gives the basic logic
import tkinter as tk
#ttk has all the widgets that we want to use
#from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = ttk.Window(themename='darkly')
window.title('Demo')
#set size of window widthxheight
window.geometry('300x150')

#WIDGET 
#title      Label is a fancy word for text in tkinter
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
#the widget must be in a container [in tkinter, a master which at this moment is Window]
title_label.pack()
#method for showing title_label

#input field
input_frame=ttk.Frame(master=window)
entry_int=tk.IntVar()
entry=ttk.Entry(master= input_frame, textvariable = entry_int)
#pass the function, do not call it as the button is gonna call the function
button=ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=15)
button.pack(side='left')
input_frame.pack(pady=15)


#output
output_string = tk.StringVar()
output_label=ttk.Label(master=window,
                    text='Output', 
                    font='Calibri 20',
                    textvariable = output_string)
output_label.pack(pady=5)
#run
window.mainloop()