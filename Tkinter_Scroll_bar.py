import tkinter
from tkinter import *

app=Tk()
app.title('success')
app.geometry('600x600')

parent_window=Frame(app,height=600,width=600,bg='lightgreen')
parent_window.pack(expand=True,fill=BOTH)

vertical_scrl=Scrollbar(parent_window)
canvas=Canvas(parent_window,bg='blue',yscrollcommand=vertical_scrl.set)
vertical_scrl.config(command=canvas.yview)
vertical_scrl.pack(side='right',fill='y')

child_window=Frame(parent_window)
canvas.pack(expand=1,fill=BOTH)

canvas.create_window(0,0,window=child_window)

for x in range(0,100):
    Label(child_window,text=x).pack()
parent_window.update()
canvas.config(scrollregion=canvas.bbox('all'))

app.mainloop()
