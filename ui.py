import libs
import func
from customtkinter import *

WEIGHT = 400
HEIGHT = 300

def create_ui():
    root = CTk()
    root.geometry(f'{WEIGHT}x{HEIGHT}')
    root.title('Password generate')
    root.option_add('*Font', 'Times')
    root.grid_columnconfigure(0, weight=1)

    text_label = CTkLabel(root, text='Password generate', font=('', 18))
    text_label.grid(column=0, row=0, sticky='n', pady=(10, 5))

    result_label = CTkEntry(root, width=250)
    result_label.grid(column=0, row=1, sticky='n', pady=5)

    btn_frame = CTkFrame(root, fg_color='transparent')
    btn_frame.grid(column=0, row=2, sticky="n")

    gen_btn = CTkButton(btn_frame, text='Generate password', width=100, command=func.generate)
    gen_btn.pack(side=LEFT, padx=5)

    copy_btn = CTkButton(btn_frame, text='Copy result', width=120, command=func.copy)
    copy_btn.pack(side=LEFT, padx=5)

    root.mainloop()
    