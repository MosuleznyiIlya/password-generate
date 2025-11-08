from customtkinter import *

WEIGHT = 500
HEIGHT = 500

def create_ui():
    root = CTk()
    root.geometry(f'{WEIGHT}x{HEIGHT}')
    root.title('Password generate')

    root.mainloop()
    