
from tkinter import *
from tkinter import font
import datetime as dt
from time import *
import random as rd
import cmath
from Base import *
from Calculator import *
from Schedule import *
from Diary import *


class Menu:
   __classes_list = list()
   __Buttons = ['Home page', 'Diary', 'Schedule', 'Calculator', 'Save all']
   def home_page_lbl(self):
       #initalize:
       d = datetime.now()
       d.toordinal()
       t = str(d.strftime('%H : %M : %S'))
       self.__home_page_frm = LabelFrame(self.__base.get_BaseLbl(),
                                      text='',
                                      font=('Arial Rounded MT Bold', 50),
                                      bd=3,
                                      width=100,
                                      bg='white',
                                      fg='#00B0F0',
                                      foreground='#00B0F0',
                                      relief='flat',
                                      labelanchor='n')
       self.__home_page_lbl = Label(self.__home_page_frm,
                             text='Time is above nature',
                             font=('Arial Rounded MT Bold', 20),
                             width=70,
                             bg='white',
                             fg='#0070C0',
                             foreground='#0070C0',
                             relief='flat',
                             anchor='center')
       self.update_clock()
       #pack and grid:
       self.__home_page_frm.grid(sticky='ew', columnspan=2, column=3, row=2)
       self.__home_page_lbl.pack()
   def update_clock(self):
       d = datetime.now()
       d.toordinal()
       t = str(d.strftime('%H : %M : %S'))
       self.__home_page_frm.configure(text=t)
       self.__home_page_frm.after(200, self.update_clock)
   def save_all_func(self):
       self.Schedule.save_data_func()
       self.Diary.save_data_func()
   def change_lbl(self, btn):
        if btn == 'Save all':
            self.save_all_func()
        else:
            for c in self.__classes_list:
                c.get_BaseLbl().pack_forget()
            if btn == 'Schedule':
                self.__Schedule.get_BaseLbl().pack(side='right', fill='both', expand=1)
            elif btn == 'Calculator':
                self.__calc.get_BaseLbl().pack(side='right', fill='both', expand=1)
            elif btn == 'Diary':
                self.__Diary.get_BaseLbl().pack(side='right', fill='both', expand=1)
            elif btn == 'Home page':
                self.__base.get_BaseLbl().pack(side='right', fill='both', expand=1)
   def __init__(self, master):  
       # initialize:
       self.__base = Base(master)
       self.__calc = Calculator(master)
       self.__Schedule = Schedule(master)
       self.__Diary = Diary(master)
       self.__my_menu = LabelFrame(master,
                                   text="Menu", font=('Arial Rounded MT Bold', 40),
                                   relief='groove', bg='#00B0F0',
                                   fg='WHITE')
       for btn in self.__Buttons:
           self.__btn = Button(self.__my_menu,
                                 text=btn,
                                 bd=7, relief='flat',
                                 bg='#00B0F0',
                                 fg='WHITE',
                                 font=('Arial Rounded MT Bold', 15),
                                 cursor='mouse',
                                 justify='left',
                                 command=lambda t=btn: self.change_lbl(t))
        # grid and pack:
           self.__btn.grid(sticky='w')
       self.__my_menu.pack(fill='y', side='left')
       self.__base.get_BaseLbl().pack(side='right', fill='both', expand=1)
       self.home_page_lbl()
       #bulid classes list:
       self.__classes_list.append(self.__base)
       self.__classes_list.append(self.__Diary)
       self.__classes_list.append(self.__calc)
       self.__classes_list.append(self.__Schedule)


class Main:
    def __init__(self):
        self.__root = Tk()
        self.__menu = Menu(self.__root)
        self.__root.minsize(1600, 1000)
        self.__root.mainloop()
