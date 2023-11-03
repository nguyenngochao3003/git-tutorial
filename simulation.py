import tkinter as tk
from tkinter import ttk
import random as rd
import datetime

SPACE_SIZE = 100
DATE_LENGHT = 200


class main_app():
    def __init__(self, title):
        self.app = tk.Tk()
        self.app.title = title
        self.app.columnconfigure(0, weight=4)
        self.app.columnconfigure(1, weight=1)
        self.app.columnconfigure(2, weight=10)
        self.app.grid()
        self.WIDTH = self.app.winfo_screenwidth()
        self.HEIGHT = self.app.winfo_screenheight()
        self.tab1 = ttk.Notebook(self.app, width= self.WIDTH, height= 100)
        self.tab1.grid(column=0, row=0, sticky=tk.NW)
        self.tab2 = ttk.Notebook(self.app, width=self.WIDTH, height=self.HEIGHT-100)
        self.tab2.grid(column=0, row=2, sticky=tk.NW)

        self.create_tab_ribon()
        self.create_tab_processing()
        self.create_frame_inside_tab_processing()
        self.ribbon()
        
    
    def create_tab_ribon(self):
        self.fr_planning = ttk.Frame(self.tab1)
        self.tab1.add(self.fr_planning, text='Planning')
        
        self.fr_optimization = ttk.Frame(self.tab1)
        self.tab1.add(self.fr_optimization, text='Optimization')

        self.fr_display = ttk.Frame(self.tab1)
        self.tab1.add(self.fr_display, text='Display')

        self.fr_action = ttk.Frame(self.tab1)
        self.tab1.add(self.fr_action, text='Action')

        self.fr_filter = ttk.Frame(self.tab1)
        self.tab1.add(self.fr_filter, text='Filter')

    def ribbon(self):
        button = tk.Button(self.fr_planning, text='Move', compound='left')
        button.pack(ipadx=10, ipady=10, anchor="nw")       



    def create_tab_processing(self):
        self.fr_gantt_chart = ttk.Frame(self.tab2)
        self.tab2.add(self.fr_gantt_chart, text='Resource Gantt Chart')

        self.fr_sequence = ttk.Frame(self.tab2)
        self.tab2.add(self.fr_sequence, text='Resource Sequence')
    
    def create_frame_inside_tab_processing(self):
        # Create style for the first frame
        self.frganttchart__table = ttk.Frame(self.fr_gantt_chart, width=500, height=self.HEIGHT-120,borderwidth=2, relief='groove')
        self.frganttchart__table.place(x=0, y=0)
        self.frganttchart__gantt = ttk.Frame(self.fr_gantt_chart, width=self.WIDTH-500, height=self.HEIGHT-120,borderwidth=2, relief='groove')
        self.frganttchart__gantt.place(x=600, y=0)

    def run(self):
        self.app.mainloop()


class table():
    def  __init__(self, container):
        columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(container, columns=columns, show='tree headings', height = 20)
        
        self.create_table(container=container)

    def create_table(self, container):
        columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(container, columns=columns, show='tree headings', height = 20)

        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 14))
        style.configure("Treeview", font=(None, 10))
        style.configure('Treeview', rowheight=40)

        self.tree.heading('#0', text='Department')
        self.tree.heading('first_name', text="First Name")
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text="Email")

        self.tree.column('#0', width=200, anchor=tk.W)
        self.tree.column('first_name', width=60, anchor=tk.CENTER)
        self.tree.column('last_name', width=100, anchor=tk.CENTER)
        self.tree.column('email', width=200, anchor=tk.CENTER)

        self.tree.insert('', tk.END, iid=0, text="administration", open=True, values=('hao', 'nguyen ngoc', 'nguyenngochao@gmail.com'))
        self.tree.insert('', tk.END, iid=1, text="accounting", open=True, values=('hien', 'tran thi dieu', 'tranthidieuhien@gmail.com'))
        self.tree.insert('', tk.END, iid=2, text="technical", open=True, values=('hien', 'tran thi dieu', 'tranthidieuhien@gmail.com'))
        self.tree.insert('', tk.END, iid=3, text="R&D", open=True, values=('hien', 'tran thi dieu', 'tranthidieuhien@gmail.com'))
        self.tree.insert('', tk.END, iid=4, text="wood engineering", open=True, values=('phong', 'tran lanh', 'tranlanhphong@gmail.com'))
        self.tree.insert('', tk.END, iid=5, text="tech pack", open=True, values=('thuong', 'mai van', 'maivanlanh@gmail.com'))

        contacts = []
        for i in range(1, 50):
            contacts.append((f"first name {i}", f"last name {i}", f"email{i}.com"))
        
        i = 6
        j = 2
        for contact in contacts:
            self.tree.insert('', tk.END, iid=i, text='tech pack', open=True, values=contact )
            self.tree.move(i, 3, j)
            i += 1
            j += 1

        self.tree.move(4, 3, 0)
        self.tree.move(5, 3, 1)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        return self.tree
    
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # infor = showinfo(title='Information', message=','.join(record))

        
class create_gantt():

    def __init__(self, container, width, height):
        self.canvas = tk.Canvas(master=container, width=width, height=height, relief='groove', borderwidth=2)
        self.canvas.grid(row=0, column=0, sticky=tk.N)

    def time_line(self):
        
        # Create dates timeline
        start_date = datetime.date.today()
        
        # delta time
        delta = datetime.timedelta(days=1)
        
        y0, y1 = 30, 60
        y_center = (y1 - y0) / 2 + y0
        x0 = 0
        delta = datetime.timedelta(days=1)

        for i in range(1, 8):
            x1 = x0 + DATE_LENGHT
            x_center = (x1 - x0) / 2 + x0
            t = self.canvas.create_rectangle(x0, y0, x1, y1, fill='green') 
            self.canvas.create_text(x_center, y_center, text=start_date.strftime("%a-%d"))
            start_date += delta
            x0 = x1

        # create week timeline
        start_date = datetime.date.today()
        delta = datetime.timedelta(days=1)
        x0, x1 = 0, 0
        y0, y1 = 0, 30
        y_center = (y1 - y0) / 2 + y0
        count = 0
        for i in range(1, 8):
            time_week = start_date.strftime("%W")
            start_date += delta
            print(start_date.strftime("%W"))
            # next_timeweek = start_date.strftime("%W")
            count += 1
            if time_week != start_date.strftime("%W") or i == 7:
                x1 = x0 + DATE_LENGHT * count
                x_center = (x1 - x0) / 2 + x0
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="gray")
                self.canvas.create_text(x_center, y_center, text=time_week)
                x0 = x1
                count = 0

                
         

    # assum 1 day = 8h
    # start from 8h to 16h
    def create_gantt_chart(self, data):
        # data = [('op1', 4, 8),
        # ('op1', 9, 10)]
        
        #create time line
        y0 = 50
        y1 = 80
        x0_coordinate = 50
        day_width = DATE_LENGHT
        shift_hours = 10
        for i in range(0, len(data)):
            end = data[i][2]
            start = data[i][1]
            op_name = data[i][0]
            duration = end - start 
            timeline_width = duration / shift_hours * day_width    
            x0 = start /shift_hours * day_width        
            x1 = x0 + timeline_width
            x_center = (x1 - x0) / 2 + x0
            y_center = (y1 - y0)/2 + y0
            rec_color = self.random_color_generator()
            self.canvas.create_rectangle(x0,y0, x1, y1, fill="brown")

            self.canvas.create_text(
                (x_center, y_center),
                text=op_name,
                fill="black",
                font='tkDefaeultFont 10',
                anchor=tk.CENTER,
                width=timeline_width )


    def move(self):
        pass 


    def connector_straingth(self, rec1, rec2):
        print("rec1: ",self.canvas.coords(rec1))
        #toa do x2, y2 cua rec 1

        coords1 = self.canvas.coords(rec1)

        x1, y1 = coords1[2], (coords1[3] - coords1[1]) / 2 + coords1[1] 


        coords2 = self.canvas.coords(rec2)

        x2, y2 = coords2[0], (coords2[3] - coords2[1]) /2 + coords2[1]

        print('x1: ', x1, ' x2: ', x2)
        self.canvas.create_line(x1, y1, x2, y2)
        
 
    @staticmethod
    def random_color_generator():
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        return (r, g, b)
    



class create_scroll():
    def __init__(self, container, parent):
        self.scroll = ttk.Scrollbar(container, orient='vertical', command=parent.yview)
        self.scroll.grid(row=0, column=1, sticky=tk.NS)
        parent.configure(yscrollcommand=self.scroll.set)
 
        
if __name__ == "__main__":
    app = main_app('app')
    tables =  table(app.frganttchart__table)
    gantt = create_gantt(app.frganttchart__gantt, app.WIDTH-500, app.HEIGHT-120)
    data = [('op1sdssssssssss', 4, 8),
            ('op1sssssssss', 9, 10)]
    gantt.create_gantt_chart(data=data)
    gantt.time_line()
    # scroll = create_scroll(app, tables)
    app.run()
    
    

    
    