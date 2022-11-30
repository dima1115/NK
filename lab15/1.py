import tkinter as tk
import json
window=tk.Tk()
fr = tk.Frame(master=window, width=350, height=480)
fr.pack()
inf=[]
def check():
    inf.append(entry_name.get())
    inf.append(entry_name2.get())
    with open('propusk.json', 'a') as f:
        json.dump(inf, f)
    entry_name.delete(0, tk.END)
    entry_name2.delete(0, tk.END)
entry_name=tk.Entry(fg='black',bg='white')
entry_name.place(x=75, y=200)
entry_name2=tk.Entry(fg='black',bg='white')
entry_name2.place(x=75, y=100)
button = tk.Button(text="Добавити",width=10,height=1, command=check)
button.place(x=110, y=300)
window.mainloop()
