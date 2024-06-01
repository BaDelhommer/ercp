import tkinter as tk
from tkinter import ttk
import requests
from functools import partial

def fetch_items():
    url = 'https://api.erdb.wiki/v1/latest/armaments/'
    response = requests.get(url)
    return response.json()

def show_item_details(combo, event):
    selected_item = combo.get()
    for item in list(items.keys()):
        if item == selected_item:
            details_label.config(text=f"Requirements: {items[item]['requirements']}")
            break

items = fetch_items()

root = tk.Tk()
root.title('Elden Ring Weapon Selector')

main_hand_combo = ttk.Combobox(root, values=list(items.keys()))
main_hand_combo.pack()
main_hand_combo.bind('<<ComboboxSelected>>', partial(show_item_details, main_hand_combo))

details_label = tk.Label(root, text='')
details_label.pack()

attribution_label = tk.Label(root, text='Data provided by Elden Ring Database')
attribution_label.pack()

root.mainloop()