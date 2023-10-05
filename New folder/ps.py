import PySimpleGUI as sg
import pandas as pd
import sqlite3
sg.theme('LightBlue4')

df = pd.read_excel("data empty.xlsx")
table_data = df.values.tolist()
table_header = df.columns.values.tolist()
print(table_header)

layout = [
    [sg.Text("Enter Employee Information", background_color='Green', text_color='Yellow', justification="Left")],
    [sg.Text('Emp ID', size=(10,1)),sg.Input(key="ID",size=(41,4)), sg.Text("Department",size=(11,1)),
     sg.Combo(['Hành Chính', 'Kỹ thuật', 'Kế hoạch tài chính', 'Truyền thông'],key='Department',size=(58,5))],
     [sg.Text('Emp Name', size=(10,1)),sg.Input(key="Name",size=(41,4)), sg.Text("City",size=(11,1)),
     sg.Input(key='City',size=(58,1)) ],
     [sg.Text('Gender',size=(10,1)),sg.Radio("Male","g",True,key='g1'),sg.Radio("Female","g",key="g2")],
     [sg.Button('Save', key='Save'), sg.Button('Exit',key='Exit')],
    
     [sg.Table(values=table_data,
               headings= table_header,
               key="Table",
               row_height=30,
               justification='center',
               expand_x=True,
               expand_y=True,
               )]
    
]

window = sg.Window("Automatied Data Entry Form", layout)


while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Save':
        values['Gender'] = 'Male' if values['g1'] else "Female"
        del values['g1']
        del values['g2']
        del values['Table']
        df = df._append(values, ignore_index=True)
        df.to_excel("data empty.xlsx", index=False)
        val = df.values.tolist()

        

        window["Table"].update(values = val)