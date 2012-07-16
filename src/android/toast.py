#!/usr/bin/env python

import Tkinter


def center_window(app):
    w = app.winfo_screenwidth()
    h = app.winfo_screenheight()
    rootsize = tuple(int(_) for _ in app.geometry().split('+')[0].split('x'))
    x = w/2 - rootsize[0]/2
    y = h/2 - rootsize[1]/2
    return "%dx%d+%d+%d" % (rootsize + (x, y))


def show_toast(message):

    master = Tkinter.Tk()
    
    label = Tkinter.Label(text=message).pack(expand=True)
    
    frame = Tkinter.Frame(master, 
                          width=320, height=160, 
                          bg="", colormap="new")
    frame.pack(fill=Tkinter.X, padx=5, pady=5)
    frame.after(5000, master.destroy)
    
    master.update_idletasks()
    master.geometry(center_window(master))
    master.mainloop()