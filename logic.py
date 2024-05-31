import requests

def fetch_armaments():
    url = "https://api.erdb.wiki/v1/latest/armaments/"
    response = requests.get(url)
    return response.json()

def fetch_armor():
    url = "https://api.erdb.wiki/v1/latest/armor/"
    response = requests.get(url)
    return response.json()

def fetch_spells():
    url = "https://api.erdb.wiki/v1/latest/spells/"
    response = requests.get(url)
    return response.json()

def calculate_requirements(selected_items, items):
    requirements = {"strength": 0, "dexterity": 0, "intelligence": 0, "faith": 0}

    for item_name in selected_items:
        item = items.get(item_name, {})
        if not item:
            continue

        item_req = item.get('requirements', {})
        for stat, value in item_req.items():
            if value > requirements.get(stat, 0):
                requirements[stat] = value

    return requirements