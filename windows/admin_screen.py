import tkinter as tk
import sys
import os
import threading

def run_sub(): os.system('pythonw windows\\subjects.py')
def run_fac(): os.system('pythonw windows\\faculty.py')
def run_stud(): os.system('pythonw windows\\student.py')
def run_sch(): os.system('pythonw windows\\scheduler.py')
def run_tt_s(): os.system('pythonw windows\\timetable_stud.py')
def run_tt_f(): os.system('pythonw windows\\timetable_fac.py')

ad = tk.Tk()
ad.geometry('1800x1830')

ad.title('Administrator')

tk.Label(
    ad,
    text='A D M I N I S T R A T O R''(KUNCHAPU GOWRISAI)',
    font=('Consolas', 20, 'bold'),
    pady=10
).pack()

tk.Label(
    ad,
    text='You are the Administrator',
    font=('Consolas', 12, 'italic'),
).pack(pady=9)

modify_frame = tk.LabelFrame(text='Modify', font=('Consolas'), padx=50)
modify_frame.place(x=500, y=200)

tk.Button(
    modify_frame,
    text='Subjects',
    font=('Consolas'),
    bg='green',
    fg='black',
    command=run_sub
).pack(pady=50)

tk.Button(
    modify_frame,
    text='Faculties',
    font=('Consolas'),
    bg='pink',
    fg='black',
    command=run_fac
).pack(pady=50)

tk.Button(
    modify_frame,
    text='Students',
    font=('Consolas'),
    bg='yellow',
    fg='black',
    command=run_stud
).pack(pady=50)

tt_frame = tk.LabelFrame(text='Timetable', font=('Consolas'), padx=50)
tt_frame.place(x=800, y=200)

tk.Button(
    tt_frame,
    text='Schedule Periods',
    font=('Consolas'),
    bg='green',
    fg='black',
    command=run_sch
).pack(pady=50)

tk.Button(
    tt_frame,
    text='View Section-Wise',
    font=('Consolas'),
    bg='pink',
    fg='black',
    command=run_tt_s
).pack(pady=50)

tk.Button(
    tt_frame,
    text='View Faculty-wise',
    font=('Consolas'),
    bg='yellow',
    fg='black',
    command=run_tt_f
).pack(pady=50)


tk.Button(
    ad,
    text='Quit',
    font=('Consolas'),
    bg='red',
    fg='black',
    command=ad.destroy
).place(x=730, y=650)

ad.mainloop()
