# tkinter :- module and library :- collection of modules

# import tkinter for creating GUI apps.

import tkinter as tk

from tkinter import filedialog, messagebox

# Main window code
root= tk.Tk()
root.title("Simpel Text Editor")
root.geometry("800x600")

# Creat text area
text= tk.Text(
    root,
    wrap= tk.WORD,
    font= ("Hrlvetica", 15,)
)

text.pack(expand=True,fill=tk.BOTH)

# Main logic starts now

# Function 1 - to creat a new file
def new_file():
    text.delete(1.0, tk.END)

# Function 2 - to open a new file
def open_file():
    # Opne fle dialoge
    file_path= filedialog.askopenfilename(
        defaultextension = "txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        #open selected file
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Fubction 3 - save file

def save_file():
    #open save file dialog
    file_path= filedialog.askopenfilename(
        defaultextension= "txt",
        filetypes= [("Text File", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully")

# Creat Menu bar
menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

# New , opne , Save , Exit

# Add file menu to menu bar
menu.add_cascade(label="File", menu= file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Starts and keeps windows open
root.mainloop()