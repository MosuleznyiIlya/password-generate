import random
import string
import ui

def generate(ui_refs):
    lenght = int(ui_refs['len_entry'].get())
    chars=''
    if ui_refs['use_digits'].get():
        chars += '0123456789'
    if ui_refs['use_uppercase'].get():
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if ui_refs['use_lowercase'].get():
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if ui_refs['use_symbols'].get():
        chars += '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    if not chars:
        ui.show_notification('Select at least one character set', ui_refs['notification_label'], ui_refs['root'])
        return
    password=''.join([random.choice(chars) for _ in range(lenght)])
    ui_refs['result_label'].delete(0, 'end')
    ui_refs['result_label'].insert(0, password)
def copy(ui_refs):
    text = ui_refs["result_label"].get()
    if not text:
        ui.show_notification("Нечего копировать", ui_refs["notification_label"], ui_refs["root"])
        return
    ui_refs["root"].clipboard_clear()
    ui_refs["root"].clipboard_append(text)
    ui_refs["root"].update()
    ui.show_notification("Скопировано!", ui_refs["notification_label"], ui_refs["root"])
def slider_changed(value, entry, slider):
    entry.delete(0, 'end')
    entry.insert(0, str(int(value)))
def entry_changed(event, entry, slider):
    try:
        value = int(entry.get())
        if 6 <= value <= 999:
            slider.set(value)
    except ValueError:
        pass