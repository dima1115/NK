import tkinter as tk
win=tk.Tk()
win['bg']='black'
def info():
    with open('settings.txt', 'w') as f:
        f.write(win.geometry())
    with open('settings.txt', 'a') as f:
        f.write(' ')
        f.write(win['background'])
L=tk.Label(text='Доброго дня!', foreground='brown',background="black")
button = tk.Button(text="ПУСК",width=25, foreground="red",background='black', command=info)
L.pack()
button.pack()
win.mainloop()
