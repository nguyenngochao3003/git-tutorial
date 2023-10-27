import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window()
app.geometry('600x500')

label = ttk.Label(app, text="Contact Information", font=('Arial', 20, 'bold'))
label.pack(pady=30)

name_frame = ttk.Frame(app)
name_frame.pack(pady=15, padx=10, fill= 'x')

name_label = ttk.Label(name_frame, text='Name', font=('arial', 14))
name_label.pack(padx=5, side='left')

name_entry = ttk.Entry(name_frame, font=('arial', 16))
name_entry.pack(padx=5, side='left', expand=True, fill='x')

email_frame = ttk.Frame(app)
email_frame.pack(pady=15, padx=10, fill= 'x')

email_label = ttk.Label(email_frame, text='Email', font=('arial', 14))
email_label.pack(padx=5, side='left')

email_entry = ttk.Entry(email_frame, font=('arial', 16))
email_entry.pack(padx=5, side='left', expand=True, fill='x')

check_frame = ttk.Frame(app).pack(pady=15, padx= 10, fill='x')
check_button = ttk.Checkbutton(check_frame, bootstyle='toggle-round', text='Remember Infor?').pack(padx=10, side='left')

# button_frame = ttk.Frame(app).pack(pady=50, padx= 10, fill='x')

# summit_button = ttk.Button(button_frame, text='Summit', bootstyle='success').pack(padx=10, side='left')
# cancel_button = ttk.Button(button_frame, text='Cancel', bootstyle='danger').pack(padx=10, side='left')
app.mainloop()
                  