import random
import string
import ui

def generate(ui_refs):
    pass
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
