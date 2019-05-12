from tkinter import *
from pynput import *


dict_conversion = {keyboard.Key.tab: 'tab',
                   keyboard.Key.shift: 'shift',
                   keyboard.Key.ctrl_l: 'ctrl',
                   keyboard.Key.alt_l: 'alt',
                   keyboard.Key.space: 'space',
                   '&': '1',
                   'é': '2',
                   '"': '3',
                   "'": '4',
                   '(': '5'}


def keydown(key):
    try:
        touche = key.char
    except AttributeError:
        touche = key

    if touche in dict_conversion.keys():
        touche = dict_conversion[touche]

    if touche in list_button.keys():
        list_button[touche].configure(bg='#264aff')


def keyup(key):
    try:
        touche = key.char
    except AttributeError:
        touche = key

    if touche in dict_conversion.keys():
        touche = dict_conversion[touche]

    if touche in list_button.keys():
        list_button[touche].configure(bg='#375387')


def on_click(x, y, button, pressed):
    pass


root = Tk()
root.title('keyboard input')
root.configure(bg='#00ff00')
'#264aff'
list_button = {}
list_name = [[None, '1', '2', '3', '4', '5'], ['Tab', 'A', 'Z', 'E', 'R', 'T'], [None, 'Q', 'S', 'D', 'F', 'G'], ['Shift', 'W', 'X', 'C', 'V', 'B'], ['Ctrl', 'Alt', None, 'Space']]
for ligne in list_name:
    for touche in ligne:
        if touche is None:
            pass
        else:
            list_button[touche.lower()] = Label(root, text=touche, bg='#375387', relief='flat', font='Helvetica 25 bold', width=2 if touche not in ['Tab', 'Shift', 'Ctrl', 'Alt'] else 4)
            list_button[touche.lower()].grid(row=list_name.index(ligne), column=ligne.index(touche), padx=6, pady=5, columnspan=3 if touche is 'Space' else 2 if touche is 'Alt' else 1, sticky=E+W if touche is 'Space' else E)


mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
keyboard_listener = keyboard.Listener(on_press=keydown, on_release=keyup)
keyboard_listener.start()
root.mainloop()

