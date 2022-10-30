
from tkinter import *
from Main import *
from Base import *


class Schedule(Base):
    __r = 0
    __c = 0
    __days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    __day_data_dict = dict()
    __file_name = "Schedule_file.xml"
    def save_data_func(self):
        for day in range(0, 7):
            for i in range(0, self.__day_data_dict[day]['index']+1):
                if i in self.__day_data_dict[day].keys():
                    self.__day_data_dict[day][i]['text'] = self.__day_data_dict[day][i]['sub'].cget('text')
        if not os.path.isfile(self.__file_name):
            root = et.Element("Dictionaries")
            tree = et.ElementTree(root)
            day_dict = et.SubElement(root, "day_dict")
            with open(self.__file_name, "w") as files:
                tree.write(self.__file_name)
        tree = et.parse(self.__file_name)
        root = tree.getroot()
        day_dict = root.find('day_dict')
        root.remove(day_dict)
        with open(self.__file_name, "w") as files:
            tree.write(self.__file_name)
        day_dict = et.SubElement(root, "day_dict")
        with open(self.__file_name, "w") as files:
            tree.write(self.__file_name)
        for day in range(0, 7):
            new_element = et.SubElement(day_dict, "day" + str(day))
            with open(self.__file_name, "w") as files:
                tree.write(self.__file_name)
            for i in range(0, self.__day_data_dict[day]['index']+1):
                if i in self.__day_data_dict[day].keys():
                    new_item = et.SubElement(new_element, "text")
                    new_item.text = str(self.__day_data_dict[day][i]['text'])
                    with open(self.__file_name, "w") as files:
                        tree.write(self.__file_name)
    def load_NewSubject(self, day):
        if os.path.isfile(self.__file_name):
            tree = et.parse(self.__file_name)
            root = tree.getroot()
            index = 'day_dict/day' + str(self.__days.index(day.cget('text'))) + '/text'
            items = root.findall(index)
            for item in items:
                if item.text is not None:
                    self.set_NewSubject(day, item.text)
        else:
            self.set_NewSubject(day, 'subject')
    def change_title(self, sub, sub_t):
        if sub_t.get() == '':
            sub.grid_forget()
        sub.configure(text=sub_t.get())
        sub_t.delete(0, END)
    def set_NewSubject(self, day, text):
        #initialize:
       self.__sub = LabelFrame(day,
                                 text=text,
                                 font=('Arial Rounded MT Bold', 15),
                                 bd=1,
                                 bg='white',
                                 fg='#002060',
                                 foreground='#002060',
                                 relief='sunken',
                                 width=170,
                                 height=150)
       self.__sub_title = Entry(self.__sub,
                                 font=('Arial Rounded MT Bold', 10),
                                 bd=1,
                                 bg='white',
                                 fg='#002060',
                                 relief='solid',
                                 width=15)
       self.__sub_title_btn = Button(self.__sub,
                                      text='change title',
                                      font=('Arial Rounded MT Bold', 10),
                                      bd=0,
                                      bg='white',
                                      fg='#002060',
                                      relief='flat',
                                      width=10,
                                      height=1,
                                      command=lambda sb=self.__sub, sub_t=self.__sub_title: self.change_title(sb, sub_t))
       #grid:
       if self.__days.index(day.cget('text')) in self.__day_data_dict.keys():
            self.__sub.grid(row=self.__day_data_dict[self.__days.index(day.cget('text'))]['row']+1, column=0)
            self.__day_data_dict['add_sub' + str( self.__days.index(day.cget('text')))].grid_configure(
                row=self.__day_data_dict[self.__days.index(day.cget('text'))].get('row') + 2)
            self.__day_data_dict[self.__days.index(day.cget('text'))]['row'] += 1
       else:
           self.__sub.grid(row=0, column=0)

       self.__sub_title.grid(row=0, column=0)
       self.__sub_title_btn.grid(row=0, column=1)
       #data:
       if self.__days.index(day.cget('text')) in self.__day_data_dict.keys():
            self.__day_data_dict[self.__days.index(day.cget('text'))]['row'] += 1
            self.__day_data_dict[self.__days.index(day.cget('text'))]['index'] += 1
            sub_data_dict = {'text': text, 'sub': self.__sub, 'title': self.__sub_title, 'title_btn': self.__sub_title_btn}
            self.__day_data_dict[self.__days.index(day.cget('text'))].update(
                {self.__day_data_dict[self.__days.index(day.cget('text'))]['index']: sub_data_dict})
       else:
            sub_data_dict = {0: {'text': text, 'sub': self.__sub, 'title': self.__sub_title, 'title_btn': self.__sub_title_btn}, 'row': 0, 'index': 1}
            self.__day_data_dict.update({self.__days.index(day.cget('text')): sub_data_dict})
    def __init__(self, master):
        super().__init__(master)
        #initialize:
        self.__week = LabelFrame(self.get_BaseLbl(),
                                   text='Schedule week',
                                   font=('Arial Rounded MT Bold', 25),
                                   bd=1,
                                   bg='white',
                                   fg='#00B0F0',
                                   foreground='#00B0F0',
                                   relief = 'groove',
                                   labelanchor='n')
        self.__week.grid(row=1, column=4)
        for day in self.__days:
            day = LabelFrame(self.__week,
                             text=day,
                             font=('Arial Rounded MT Bold', 20),
                             bd=2,
                             bg='white',
                             fg='#0070C0',
                             foreground='#0070C0',
                             relief='flat',
                             width=175,
                             height=150)
            addSubject_btn = Button(day,
                                    text='add subject',
                                    font=('Arial Rounded MT Bold', 12),
                                    bd=0,
                                    bg='white',
                                    fg='#0070C0',
                                    relief='groove',
                                    width=12,
                                    height=1,
                                    anchor='w',
                                    command=lambda d=day: self.set_NewSubject(d, 'subject'))
            #grids:
            day.pack(side='left', anchor='nw')
            addSubject_btn.grid(sticky='s', row=1000)
            self.__c += 1
            #data:
            self.__day_data_dict.update({'add_sub' + str(self.__days.index(day.cget('text'))): addSubject_btn})
            self.load_NewSubject(day)
        self.get_save_btn().configure(command=self.save_data_func)
