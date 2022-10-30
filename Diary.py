
from tkinter import *
from Main import *
from Base import *
from datetime import *
from tkcalendar import *
from tkinter.tix import ButtonBox, LabelEntry
import xml.etree.ElementTree as et
from xml.dom import  *
from xml import etree
import os
import os.path

class Diary(Base):
    #time parameters:
    __date = datetime.now()
    __date.toordinal()
    __year = int(__date.strftime('%Y'))
    __month = int(__date.strftime('%m'))
    __day = int(__date.strftime('%d'))
    #to do list parameters:
    __index = 0
    __check_buttons = dict()
    __State = dict()
    #diary parameters:
    __diary_dict = dict()
    __diary_index = 0
    #save parameters:
    __save_data_list = list()
    __file_name = "Dairy_file.xml"

    #functions:
    def save_data_func(self):
        for index in self.__diary_dict:
            self.__diary_dict[index]['text_box']=self.__diary_dict[index]['box'].get("1.0",END)
        if not os.path.isfile(self.__file_name):
            root = et.Element("Dictionaries")
            tree = et.ElementTree(root)
            diary_dict = et.SubElement(root, "diary_dict")
            TO_DO_dict = et.SubElement(root, "TO_DO_dict")
            with open(self.__file_name, "w") as files:
                tree.write(self.__file_name)
        tree = et.parse(self.__file_name)
        root = tree.getroot()
        diary_dict = root.find('diary_dict')
        TO_DO_dict = root.find('TO_DO_dict')
        root.remove(diary_dict)
        root.remove(TO_DO_dict)
        with open(self.__file_name, "w") as files:
            tree.write(self.__file_name)
        diary_dict = et.SubElement(root, "diary_dict")
        TO_DO_dict = et.SubElement(root, "TO_DO_dict")
        with open(self.__file_name, "w") as files:
            tree.write(self.__file_name)
        for i in self.__diary_dict:
            if len(self.__diary_dict[i]['text_box']) > 1:
                new_text = et.SubElement(diary_dict,"text")
                new_text.text = self.__diary_dict[i]['text']
                new_text_box = et.SubElement(diary_dict,"text_box")
                new_text_box.text = self.__diary_dict[i]['text_box']
                with open(self.__file_name, "w") as files:
                    tree.write(self.__file_name)
        for i in self.__State:
            if self.__State[i].get() == 0:
                new_item = et.SubElement(TO_DO_dict, "text")
                new_item.text = self.__check_buttons[i].cget('text')
                with open(self.__file_name, "w") as files:
                    tree.write(self.__file_name)
    def load_data_func(self):
        if os.path.isfile(self.__file_name):
            tree = et.parse(self.__file_name)
            root = tree.getroot()
            new_dict = root.findall('diary_dict')
            for item in new_dict:
                if item.find('text') != None :
                    self.add_first_text_label(str(item.find('text').text) , str(item.find('text_box').text) )
            new_dict = root.findall('TO_DO_dict')
            for item in new_dict:
                if item.find('text') != None :
                    self.load_note_btn(self.__ToDo_lbl, str(item.find('text').text))
        else:
            self.add_text_label(self.__calender_lbl.get_date(),'')
    def add_first_text_label(self,date,text):
        # initialize:
        self.__text_lbl = LabelFrame(self.get_BaseLbl(),
                                   text=date,
                                   font=('Arial Rounded MT Bold', 25),
                                   bd=2,
                                   height=250,
                                   width=1200,
                                   bg='white',
                                   fg='#00B0F0',
                                   foreground='#00B0F0',
                                   relief='groove',
                                   labelanchor='nw')
        self.__text_box = Text(self.__text_lbl,
                             font=('Arial Rounded MT Bold', 15),
                             bd=2,
                             height=25,
                             width=90,
                             bg='white',
                             fg='#00B0F0',
                             foreground='#00B0F0',
                             relief='flat')
        self.__text_box.insert("1.0", text)
        self.__diary_dict.update({self.__diary_index: {'text': date, 'lbl': self.__text_lbl, 'box': self.__text_box,
                                                   'text_box': self.__text_box.get("1.0",END)}})
        self.__diary_index += 1
        # grid:
        self.__text_lbl.grid(row=4, column=3, columnspan=2)
        self.__text_box.pack(fill='x')
    def add_text_label(self,date,text):
        if len(self.__diary_dict) == 0:
            self.add_first_text_label(date, text)
        else:
            flag = 1
            self.__temp = self.__diary_dict[0]['text']
            for i in self.__diary_dict:
                self.__diary_dict[i]['lbl'].grid_forget()
                if self.__diary_dict[i]['text'] == date:
                    self.__diary_dict[i]['lbl'].grid(row=4, column=3,columnspan=2)
                    flag = 0
            if flag:
                self.add_first_text_label(date,text)
    def delete_Node(self):
        for i in range(0, len(self.__State.keys())):
            if self.__State[i].get() == 1:
                self.__check_buttons[i].pack_forget()
    def load_note_btn(self,sub,text):
        self.__State.update({self.__index: IntVar()})
        self.__sub_NoteBtn = Checkbutton(sub,
                                       text=text,
                                       font=('Arial Rounded MT Bold', 10),
                                       bd=1,
                                       bg='white',
                                       fg='#002060',
                                       relief='flat',
                                       height=1,
                                       onvalue=1,
                                       offvalue=0,
                                       var=self.State[self.__index],
                                       command=self.delete_Node
                                       )
        self.__sub_NoteBtn.pack(side='bottom')
        self.__check_buttons.update({self.__index: self.__sub_NoteBtn})
        self.__index += 1
    def add_note_btn(self,sub, sub_title):
        self.__State.update({self.__index: IntVar()})
        self.__sub_NoteBtn = Checkbutton(sub,
                                  text=sub_title.get(),
                                  font=('Arial Rounded MT Bold', 10),
                                  bd=1,
                                  bg='white',
                                  fg='#002060',
                                  relief='flat',
                                  height=1,
                                  onvalue=1,
                                  offvalue=0,
                                  var=self.__State[self.__index],
                                  command= self.delete_Node
                                  )
        self.__sub_NoteBtn.pack(side = 'bottom')
        self.__check_buttons.update({self.__index: self.__sub_NoteBtn})
        self.__index += 1
        sub_title.delete(0, END)
    def __init__(self, master):
        super().__init__(master)

        # initialize:
        self.__calender_lbl = Calendar(self.get_BaseLbl(),
                                     selectmode='day',
                                     year= self.__year,
                                     month= self.__month,
                                     day = self.__day,
                                     font=('Arial Rounded MT Bold', 10),
                                     firstweekday= 'sunday',
                                     background='blue',
                                     foreground='white',
                                     headersbackground= '#00B0F0',
                                     relief='groove')
        self.__open_diary_btn = Button(self.get_BaseLbl(),
                                        text= 'open diary',
                                        font=('Arial Rounded MT Bold', 10),
                                        bd=2,
                                        bg='white',
                                        fg='#002060',
                                        relief='groove',
                                        width=10,
                                        height=1,
                                        command= lambda : self.add_text_label(self.__calender_lbl.get_date(),''))
        self.__ToDo_lbl = LabelFrame(self.get_BaseLbl(),
                                    text = 'To Do list :',
                                    font = ('Arial Rounded MT Bold', 25),
                                    height=5,
                                    width=7,
                                     bd = 2,
                                    bg = 'white',
                                    fg = '#00B0F0',
                                    foreground = '#00B0F0',
                                    relief = 'groove')
        self.__sub_NodeBtn = Entry(self.__ToDo_lbl,
                            font=('Arial Rounded MT Bold', 10),
                            bd=1,
                            bg='white',
                            fg='#002060',
                            relief='solid',
                            width=15)
        self.__sub_AddNote_btn = Button(self.__ToDo_lbl,
                                 text='add',
                                 font=('Arial Rounded MT Bold', 10),
                                 bd=0,
                                 bg='white',
                                 fg='#002060',
                                 relief='raised',
                                 width=5,
                                 height=1,
                                 command=lambda sub=self.__ToDo_lbl, sub_t=self.__sub_NodeBtn: self.add_note_btn(sub, sub_t))
        self.add_vertical_scrollbar(self.__ToDo_lbl)
        self.get_save_btn().configure(command=self.save_data_func)
        self.load_data_func()
        #pack:
        self.__calender_lbl.grid(row=2,column=3)
        self.__ToDo_lbl.grid(row=2,column=4)
        self.__open_diary_btn.grid(row=3,column=3)
        self.__sub_NodeBtn.pack(side='top')
        self.__sub_AddNote_btn.pack(side='top')
