from tkinter import *
from Main import *
import xml.etree.ElementTree as et
from xml.dom import *
from xml import etree
import os
import os.path


class Base:
    #functions:
    def add_vertical_scrollbar(self, master):
        ver_scrollbar = Scrollbar(master, orient="vertical")
        ver_scrollbar.pack(side="right", fill="y")
    def add_horizontal_scrollbar(self, master):
        hor_scrollbar = Scrollbar(master, orient="horizontal")
        hor_scrollbar.pack(side="bottom", fill="x")
    def __init__(self, master):
        # initialize:
        self.__BaseLbl = LabelFrame(master, text="Home", font=('Arial Rounded MT Bold', 40),
                                      relief='groove', bg='WHITE',
                                      fg='#00B0F0')
        self.__save_btn = Button(self.__BaseLbl,
                                    text='save',
                                    bd=7, relief='flat',
                                    bg='WHITE',
                                    fg='#00B0F0',
                                    font=('Arial Rounded MT Bold', 10),
                                    cursor='mouse',
                                    anchor='nw')
        # grid and pack:
        self.__save_btn.grid(row=0, column=0)
    #accessors:
    def set_BaseLbl(self, new_lbl):
        self.__BaseLbl = new_lbl
    def set_save_btn(self, new_btn):
        self.__save_btn = new_brn
    #outators:
    def get_BaseLbl(self):
        return self.__BaseLbl
    def get_save_btn(self):
        return self.__save_btn
