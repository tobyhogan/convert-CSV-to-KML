import tkinter as tk


win = tk.Tk()
win.title("CSV to KML Converter")
win.config(bg="black")
win.resizable(False, False)
win.geometry('800x500')



app_title = tk.Label(win, text="CSV to KML Converter", fg="#fff", highlightbackground="#fff")
app_title.config(font=("Courier", 14))
app_title.pack()



win.lift()
win.attributes('-topmost', True)
# win.attributes('-topmost', False)

win.after(1, lambda: win.focus_force())


win.mainloop()