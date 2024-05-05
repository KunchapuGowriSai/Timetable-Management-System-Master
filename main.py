import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter as Tk
import os, sys
sys.path.insert(0, 'windows/')
import timetable_stud
import timetable_fac
import sqlite3
from tkinter import *
from PIL import ImageTk, Image  



def challenge():
    conn = sqlite3.connect(r'files/timetable.db')
    
   

    user = str(combo1.get())
    if user == "Student":
        cursor = conn.execute(f"SELECT PASSW, SECTION, NAME, ROLL FROM STUDENT WHERE SID='{id_entry.get()}'")
        cursor = list(cursor)
        if len(cursor) == 0:
            messagebox.showwarning('Bad id', 'No such user found!')
        elif passw_entry.get() != cursor[0][0]:
            messagebox.showerror('Bad pass', 'Incorret Password!')
        else:
            nw = tk.Tk()
            tk.Label(
                nw,
                text=f'{cursor[0][2]}\tSection: {cursor[0][1]}\tRoll No.: {cursor[0][3]}',
                font=('Consolas', 12, 'italic'),
            ).pack()
            m.destroy()
            timetable_stud.student_tt_frame(nw, cursor[0][1])
            nw.mainloop()

    elif user == "Faculty":
        cursor = conn.execute(f"SELECT PASSW, INI, NAME, EMAIL FROM FACULTY WHERE FID='{id_entry.get()}'")
        cursor = list(cursor)
        if len(cursor) == 0:
            messagebox.showwarning('Bad id', 'No such user found!')
        elif passw_entry.get() != cursor[0][0]:
            messagebox.showerror('Bad pass', 'Incorret Password!')
        else:
            nw = tk.Tk()
            tk.Label(
                nw,
                text=f'{cursor[0][2]} ({cursor[0][1]})\tEmail: {cursor[0][3]}',
                font=('Consolas', 12, 'italic'),
            ).pack()
            m.destroy()
            timetable_fac.fac_tt_frame(nw, cursor[0][1])
            nw.mainloop()

    elif user == "Admin":
        if id_entry.get() == 'Team' and passw_entry.get() == '10':
            m.destroy()
            os.system('python windows\\admin_screen.py')
            # sys.exit()
        else:
            messagebox.showerror('Bad Input', 'Incorret Username/Password!')
            


m = tk.Tk()

m.geometry('1800x1830')
m.title('Welcome')
img =Image.open('C:\\Users\\kunch\\OneDrive\\Pictures\\backimage.1.jpg')
bg = ImageTk.PhotoImage(img)

m.geometry("1800x1830")

# Add image
label = Label(m, image=bg)
label.place(x = 0,y = 0)


tk.Label(
    m,
    text='TIMETABLE MANAGEMENT SYSTEM',
    font=('Consolas', 20, 'bold'),
    bg="black",
    fg="white",
    wrap=400
).pack(pady=20)

tk.Label(
    m,
    text='DEVELOPED BY KUNCHAPU GOWRI SAI & TEAM',
    font=('Consolas', 20, 'bold'),
    bg="black",
    fg="white",
    wrap=400
).pack(pady=20)

tk.Label(
    m,
    text='Welcome!\nLogin to continue',
    bg="black",
    fg="white",
    font=('Consolas', 20, 'italic')
    
).pack(pady=20)

tk.Label(
    m,
    text='Username',
    bg="tomato",
    fg="white",
    font=('Consolas', 20)
).pack()

id_entry = tk.Entry(
    m,
    bg="yellow",
    fg="black",
    font=('Consolas', 15),
    width=21
)
id_entry.pack()

# Label5
tk.Label(
    m,
    text='Password:',
    bg="tomato",
    fg="white",
    font=('Consolas', 20)
).pack()

# toggles between show/hide password
def show_passw():
    if passw_entry['show'] == "●":
        passw_entry['show'] = ""
        B1_show['text'] = '●'
        B1_show.update()
    elif passw_entry['show'] == "":
        passw_entry['show'] = "●"
        B1_show['text'] = '○'
        B1_show.update()
    passw_entry.update()

pass_entry_f = tk.Frame()
pass_entry_f.pack()
# Entry2
passw_entry = tk.Entry(
    pass_entry_f,
    font=('Consolas', 15),
    bg="yellow",
    fg="black",
    width=15,
    show="●"
)
passw_entry.pack(side=tk.LEFT)

B1_show = tk.Button(
    pass_entry_f,
    text='○',
    font=('Consolas', 15, 'bold'),
    bg="black",
    fg="white",
    command=show_passw,
    padx=5
)
B1_show.pack(side=tk.LEFT, padx=20)

combo1 = ttk.Combobox(
    m,
    values=['Student', 'Faculty', 'Admin']
)
combo1.pack(pady=30)
combo1.current(0)

tk.Button(
    m,
    text='Login',
    font=('Consolas', 20, 'bold'),
    bg="black",
    fg="white",
    padx=30,
    command=challenge
).pack(pady=10)

m.mainloop()
