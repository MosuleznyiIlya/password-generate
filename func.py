import ui
import libs

def generate():
    pass
def copy(root):
    root.clipboard.clear
    root.clipboard_append(ui.result_label.get())
    root.update()
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