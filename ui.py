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
    frame = tk.Frame(parent, padx=0, pady=10)

    label = tk.Label(frame, text=name)
    label.pack(side=tk.TOP, padx=0, pady=10)

    new_combo = ttk.Combobox(frame, values=list(items_list.keys()))
    new_combo.pack(side=tk.RIGHT, fill=tk.X, expand=True)

    new_combo.bind('<KeyRelease>', partial(filter_combos, combo=new_combo, full_value_list=list(items_list.keys())))
    new_combo.bind('<Return>', partial(expand_dropdown, combo=new_combo))

    frame.pack(fill=tk.X, pady=5)
    return new_combo

def setup_ui(weapons, spells, on_button_click):
    root = tk.Tk()
    root.title('Elden Ring Stat Calculator')
    root.minsize(width=600, height=700)
    intro_label = tk.Label(root, text='Choose weapon and magic loadout to see stat requirements')
    intro_label.pack(side=tk.TOP, pady=15)

    combos = {}
    combos['main hand'] = new_combobox(root, 'Main Hand', weapons)
    combos['off hand'] = new_combobox(root, 'Off Hand', weapons)
    combos['spells'] = new_combobox(root, 'Spells', spells)

    calc_button = tk.Button(root, text='Calculate Requirements', command=on_button_click)
    calc_button.pack(pady=20)

    requirements_label = tk.Label(root, text='', background='white', fg='red')
    # requirements_label.pack(pady=10)

    return root, combos, requirements_label