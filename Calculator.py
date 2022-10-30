from tkinter import *
from turtle import width
from unittest import result
from Main import *
from Base import *
import cmath


class Calculator(Base):
    __num_buttons = list(range(9, -1, -1))
    __oper_buttons = ['C', 'AC', '%', '/', '*', '-', '+', '=', '.']
    __oper_key = ''
    __result = ''
    __prm1 = ''
    __prm2 = ''
    __r = 0
    __c = 2

    # functions:
    def num_click(self, s):
        self.__result = self.__equation_txt.get()
        self.__result += s
        if ' ' in self.__result:
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, 'invalid data')
        elif len(self.__result) > 1 and self.__result[0] == '0' and self.__result[1] != '0':
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, 'invalid data')
        elif self.__result.startswith('0') and self.__result.endswith('0'):
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, '0')
        else:
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, self.__result)
    def oper_click(self, n):
        if n == '.':
            self.__result = self.__equation_txt.get()
            if self.__result.count('.') == 0:
                self.__result += '.'
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, self.__result)
        elif n == 'C':
            self.__prm1 = ''
            self.__prm2 = ''
            self.__equation_txt.delete(0, END)
        elif n == 'AC':
            self.__result = self.__equation_txt.get()
            self.__result = self.__result[:-1]
            self.__equation_txt.delete(0, END)
            self.__equation_txt.insert(0, self.__result)
        elif self.__prm1 == '':
            self.__prm1 = self.__equation_txt.get()
            self.__equation_txt.delete(0, END)
            self.__oper_key = n
        else:
            self.__prm2 = self.__equation_txt.get()
            self.__equation_txt.delete(0, END)
            if self.__oper_key == '%':
                self.__prm1 = str(int(self.__prm1) % int(self.__prm2))
            elif self.__oper_key == '/':
                self.__prm1 = str(float(self.__prm1) / float(self.__prm2))
            elif self.__oper_key == '*':
                self.__prm1 = str(float(self.__prm1) * float(self.__prm2))
            elif self.__oper_key == '-':
                self.__prm1 = str(float(self.__prm1) - float(self.__prm2))
            elif self.__oper_key == '+':
                self.__prm1 = str(float(self.__prm1) + float(self.__prm2))
            self.__prm2 = ''
            self.__oper_key = n
            if self.__oper_key == '=':
                if self.__prm1.endswith('.'):
                    self.__prm1 += '0'
                self.__equation_txt.insert(0, self.__prm1)
                self.__prm1 = ''
                self.__oper_key = ''
    def __init__(self, master):
        super().__init__(master)
        # initialize entry:
        self.__equation_txt = Entry(self.get_BaseLbl(),
                                      background='WHITE',
                                      bd=2, fg='#00B0F0',
                                      relief='ridge',
                                      font=('Aharoni', 20),
                                      width=32, cursor='mouse')
        # grid entry:
        self.__equation_txt.grid(row=2, column=5, columnspan=4)
        # initialize numbers buttons:
        for num in self.__num_buttons:
            num = Button(self.get_BaseLbl(),
                         text=str(num),
                         bd=3, relief='ridge',
                         bg='WHITE',
                         fg='#00B0F0',
                         font=('Aharoni', 24),
                         cursor='mouse',
                         anchor='center',
                         padx=20, pady=20, width=2, height=1,
                         command=lambda s=str(num): self.num_click(s)
                         )
            # grid numbers buttons:
            if num.cget('text') == '0':
                num.grid(row=self.__r // 3 + 4, column=5)
            else:
                num.grid(row=self.__r // 3 + 4, column=self.__c % 3 + 5)
            self.__r += 1
            self.__c -= 1

        self.__r = 3
        self.__c = 0
        # initialize operations buttons:
        for oper in self.__oper_buttons:
            self.__oper = Button(self.get_BaseLbl(),
                                   text=oper,
                                   bd=3, relief='ridge',
                                   bg='WHITE',
                                   fg='#00B0F0',
                                   font=('Aharoni', 24),
                                   cursor='mouse',
                                   anchor='center',
                                   padx=20, pady=20, width=2, height=1,
                                   command=lambda s=str(oper): self.oper_click(s))
            # grid operations buttons:
            if self.__c < 3 and self.__r == 3:
                self.__oper.grid(row=self.__r, column=self.__c + 5)
                self.__c += 1
            elif self.__r == 7:
                self.__oper.grid(row=self.__r, column=self.__c + 5)
                self.__c -= 1
            elif self.__c == 3:
                self.__oper.grid(row=self.__r, column=self.__c + 5)
                self.__r += 1

