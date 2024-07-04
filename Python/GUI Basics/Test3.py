#Getting widget data & changing widgets 
'''
Two major ways to get data from a widget
 i.Tkinter variables [Should be used most of the time] (A bit advanced)
ii.get()

Lots of widget have obvious data that the user would want to get
hence there is a get method 
For example, entry has a get method that returns its text

Widgets can be updated with config [Every widget has the config method]
Label.config(text='new text')
Label['text']='some new text'
'''
import tkinter as tk
from tkinter import ttk

def btn_func():
    #get the content of the entry
    #print(entry.get())
    entry_text=entry.get()
    
    #update the label
    label['text']=entry_text
    # entry['state']='disabled'

#window
window=tk.Tk()
window.title('Getting & setting widgets')

#widgets
label=ttk.Label(master=window, text='Label')
label.pack()

entry=ttk.Entry(master=window)
entry.pack()

button=ttk.Button(master=window, text='Button', command=btn_func)
button.pack()


#run
window.mainloop()