import tkinter 
from tkinter import *
from tkinter import filedialog 

def upload_file():
    file=filedialog.askopenfilename(title="Select file" , filetypes=[("All files", '*.*'),("CSV files", '.csv')])
    # file=filedialog.askopenfilename(title="Select file" , filetypes=[("CSV files", '.csv')])

    if(file):
        file_name.set(file)
        fobj=open(file,'r')
        file_data.set(fobj.read())
    
window=Tk()
window.geometry("450x350")
window.title("Data Redundancy Detection System")
title_lbl=Label(window, text="Upload .csv file", width=30, font=("arial", 30, "bold"),bd=5)
title_lbl.grid(row=0, column=0)
button=Button(window, text="Upload File", relief=RAISED, width=20, command=upload_file)
button.grid(row=2, column=0)
file_name=StringVar()
file_data=StringVar()
my_file=StringVar()

lbl_my_file=Label(window, text="Uploaded File: ")
lbl_my_file.grid(row=3, column=0)
lbl_name=Label(window, textvariable=file_name)
lbl_name.grid(row=3, column=0)

lbl_data=Label(window, textvariable=file_data, relief=GROOVE)
lbl_data.grid(row=4, column=0)


window.mainloop()