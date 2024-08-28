import tkinter as tk
from tkinter import ttk

def convert():
    print('converted')

# window
window = tk.Tk()
window.title('Demo')
window.geometry('600x500')

# titlle
title_label = ttk.Label(master= window, text = 'First project' , font=' calibri 25 bold italic')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry= ttk.Entry(master= input_frame)
button = ttk.Button(master=  input_frame, text = 'Convert', command= 'convert')
entry.pack(side= 'left', padx=5)
button.pack()
input_frame.pack(pady=20)

#output
output_label = ttk.Label(master= window, text= 'Output', font= 'calibri 24')
output_label.pack(pady=5)



# run
window.mainloop()