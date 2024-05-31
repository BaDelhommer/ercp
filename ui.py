import tkinter as tk
from tkinter import ttk
from functools import partial

def new_combobox(parent, name, items_list, on_item_selected):
    label = tk.Label(parent, name)
    label.pack()

    combo = ttk.Combobox(parent, values=list(items_list.keys()))
    combo.pack

    combo.bind('<<ComboboxSelected>>', partial(on_item_selected, slot=name, items=items_list))

    return combo

def ui_setup(armaments, armors, spells, on_item_selected):
    root = tk.Tk()
    root.title('Elden Ring Requirements Calculator')

    combos = {}

    combos['Main Hand'] = new_combobox(root, 'Main Hand', armaments, on_item_selected)
    combos['Off Hand'] = new_combobox(root, 'Off Hand', armaments, on_item_selected)
    combos['Armor'] = new_combobox(root, 'Armor', armors, on_item_selected)
    combos['Spells'] = new_combobox(root, 'Spells', spells, on_item_selected)

    details_label = tk.Label(root, text='')
    details_label.pack()

    attribution_label = tk.Label(root, text='Data provided by Elden Ring Database')
    attribution_label.pack()

    return root, combos, details_label