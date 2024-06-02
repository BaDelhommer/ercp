import tkinter as tk
from ui import setup_ui
from logic import *

def main():
    try:
        weapons = fetch_items('https://api.erdb.wiki/v1/latest/armaments/')
        spells = fetch_items('https://api.erdb.wiki/v1/latest/spells/')
    except Exception as e:
        print(f"Error during fetch operation: {e}")
        return
    

    def on_button_click():
        main_hand_item = combos['main hand'].get()
        off_hand_item = combos['off hand'].get()
        spell_item = combos['spells'].get()

        selected_items = [main_hand_item, off_hand_item, spell_item]

        requirements = calculate_requirements(selected_items, weapons, spells)

        details_label.config(text=(
            f"strength: {requirements['strength']}, "
            f"dexterity: {requirements['dexterity']}, "
            f"faith: {requirements['faith']}, "
            f"intelligence: {requirements['intelligence']}, "
            f"arcane: {requirements['arcane']}"
        ))
        details_label.pack(pady=10)

    root, combos, details_label = setup_ui(weapons, spells, on_button_click)

    attribution_label = tk.Label(root, text='Data provided by Elden Ring Database / https://github.com/EldenRingDatabase/erdb')
    attribution_label.pack(side=tk.BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    main()