import requests

def fetch_items(url):
    response = requests.get(url)
    return response.json()

def calculate_requirements(selected_items, weapons, spells):
    requirements = {'strength': 0, 'dexterity': 0, 'faith': 0, 'intelligence': 0}
    
    for item_name in selected_items:
        if item_name in weapons:
            item = weapons.get(item_name, {})
            if not item:
                continue

            item_reqs = item.get('requirements', {})
            for stat, value in item_reqs.items():
                if value > requirements.get(stat, 0):
                    requirements[stat] = value

        elif item_name in spells:
            item = spells.get(item_name, {})
            if not item:
                continue

            item_reqs = item.get('requirements', {})
            for stat, value in item_reqs.items():
                if value > requirements.get(stat, 0):
                    requirements[stat] = value

    return requirements
            
