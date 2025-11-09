from customtkinter import *
import func

WEIGHT = 400
HEIGHT = 300

MIN_LEN = 6
MAX_LEN = 999

def show_notification(message, notification_label, root):
    notification_label.configure(text=message, text_color='green')
    notification_label.lift()
    notification_label.place(relx=0.5, rely=0.85, anchor=CENTER)
    root.after(2000, lambda: hide_notification(notification_label))

def hide_notification(notification_label):
    notification_label.configure(text='')

def create_ui():
    root = CTk()
    root.geometry(f'{WEIGHT}x{HEIGHT}')
    root.title('Password Generator')
    root.option_add('*Font', 'Times')
    root.grid_columnconfigure(0, weight=1)

    text_label = CTkLabel(root, text='Password Generator', font=('', 18))
    text_label.grid(column=0, row=0, sticky='n', pady=(10, 5))

    result_label = CTkEntry(root, width=250)
    result_label.grid(column=0, row=1, sticky='n', pady=5)

    btn_frame = CTkFrame(root, fg_color='transparent')
    btn_frame.grid(column=0, row=2, sticky='n', pady=(5, 5))

    gen_btn = CTkButton(btn_frame, text='Generate password', width=100, command=func.generate)
    gen_btn.pack(side=LEFT, padx=5)

    copy_btn = CTkButton(btn_frame, text='Copy result', width=120)
    copy_btn.pack(side=LEFT, padx=5)

    notification_label = CTkLabel(root, text='', font=CTkFont(size=14))
    notification_label.place_forget()

    len_frame = CTkFrame(root, fg_color='transparent')
    len_frame.grid(column=0, row=3, sticky='n')

    len_entry = CTkEntry(len_frame, width=35)
    len_entry.pack(side='left', padx=5, pady=10)

    len_bar = CTkSlider(len_frame, width=220, from_=MIN_LEN, to=MAX_LEN, number_of_steps=MAX_LEN - MIN_LEN)
    len_bar.pack(side='left', padx=5, pady=10)

    options_frame = CTkFrame(root)
    options_frame.grid(column=0, row=4, sticky='n')

    use_digits = BooleanVar(value=True)
    use_uppercase = BooleanVar(value=True)
    use_lowercase = BooleanVar(value=True)
    use_symbols = BooleanVar(value=False)

    checkbox_style = {
        'master': options_frame,
        'width': 80,
        'height': 20,
        'font': ('Arial', 12)
    }

    CTkCheckBox(**checkbox_style, text='0-9', variable=use_digits).pack(side=LEFT)
    CTkCheckBox(**checkbox_style, text='A-Z', variable=use_uppercase).pack(side=LEFT)
    CTkCheckBox(**checkbox_style, text='a-z', variable=use_lowercase).pack(side=LEFT)
    CTkCheckBox(**checkbox_style, text='!@#$%', variable=use_symbols).pack(side=LEFT)

    ui_refs = {
        'root': root,
        'result_label': result_label,
        'len_entry': len_entry,
        'len_bar': len_bar,
        'notification_label': notification_label,
        'use_digits': use_digits,
        'use_uppercase': use_uppercase,
        'use_lowercase': use_lowercase,
        'use_symbols': use_symbols,
    }

    gen_btn.configure(command=lambda: func.generate(ui_refs))
    copy_btn.configure(command=lambda: func.copy(ui_refs))

    len_bar.configure(command=lambda v: func.slider_changed(v, len_entry, len_bar))
    len_entry.bind('<KeyRelease>', lambda e: func.entry_changed(e, len_entry, len_bar))

    len_bar.set(MIN_LEN)
    len_entry.insert(0, str(MIN_LEN))

    root.mainloop()
    
