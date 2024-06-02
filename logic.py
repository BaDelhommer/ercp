import requests

def fetch_items(url):
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching items from {url}: {e}")
        return{}

def calculate_requirements(selected_items, weapons, spells):
    requirements = {'strength': 0, 'dexterity': 0, 'faith': 0, 'intelligence': 0, 'arcane': 0}

    all_items = {**weapons, **spells}

    for item_name in selected_items:
        item = all_items.get(item_name)
        if item:
            item_reqs = item.get('requirements', {})
            for stat, value in item_reqs.items():
                requirements[stat] = max(requirements[stat], value)

    return requirements
            
