import unittest
from logic import fetch_items

weapon = {'Blasphemous Blade': {'strength': 22, 'dexterity': 15, 'faith': 21}}
spell = {'Swarm of Flies': {'faith': 11, 'arcane': 16}}

weapons = fetch_items('https://api.erdb.wiki/v1/latest/armaments/')
spells = fetch_items('https://api.erdb.wiki/v1/latest/spells/')

class TestFetchItems(unittest.TestCase):
    def test_fetch_weapons(self):
        actual_stats = weapons['Blasphemous Blade']['requirements']
        expected_stats = weapon['Blasphemous Blade']
        self.assertEqual(actual_stats, expected_stats)

    def test_fetch_spell(self):
        actual_stats = spells['Swarm of Flies']['requirements']
        expected_stats = spell['Swarm of Flies']
        self.assertEqual(actual_stats, expected_stats)

if __name__ == '__main__':
    unittest.main()