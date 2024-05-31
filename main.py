import tkinter as tk
from tkinter import ttk
from ui import ui_setup
from logic import *

def main():
    armaments = fetch_armaments()
    armor = fetch_armor()
    spells = fetch_spells()

    def on_item_selected(event, slot, items):
        selected_items = [combos[slot].get() for slot in combos]
        requirements = calculate_requirements(selected_items, items)
        details_label.config(text=(
                             f"Str: {requirements['strength']}, "
                             f"Dex: {requirements['dexterity']}, "
                             f"Int: {requirements['intelligence']}, "
                             f"Fai: {requirements['faith']}"
        ))

    root, combos, details_label = ui_setup(armaments, armor, spells, on_item_selected)
    root.mainloop()

if __name__ == '__main__':
    main()