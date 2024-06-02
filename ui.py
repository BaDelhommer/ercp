import tkinter as tk
from tkinter import ttk
from functools import partial

def filter_combos(event, combo, full_value_list):
    value = event.widget.get().lower()
    filtered_values = [item for item in full_value_list if value in item.lower()]
    combo['values'] = filtered_values
    if filtered_values:
        combo.update_idletasks()

def expand_dropdown(event, combo):
    combo.event_generate('<Button-1>')

def new_combobox(parent, name, items_list):
    label = tk.Label(parent, text=name)
    label.pack()

    new_combo = ttk.Combobox(parent, values=list(items_list.keys()))
    new_combo.pack()

    new_combo.bind('<KeyRelease>', partial(filter_combos, combo=new_combo, full_value_list=list(items_list.keys())))
    new_combo.bind('<Return>', partial(expand_dropdown, combo=new_combo))
    return new_combo

def setup_ui(weapons, spells, on_button_click):
    root = tk.Tk()
    root.title('Elden Ring Stat Calculator')

    combos = {}
    combos['main hand'] = new_combobox(root, 'Main Hand', weapons)
    combos['off hand'] = new_combobox(root, 'Off Hand', weapons)
    combos['spells'] = new_combobox(root, 'Spells', spells)

    calc_button = tk.Button(root, text='Calculate Requirements', command=on_button_click)
    calc_button.pack()

    requirements_label = tk.Label(root, text='')
    requirements_label.pack()

    return root, combos, requirements_label