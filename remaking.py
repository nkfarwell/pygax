import sys
import fuzzywuzzy
import json

def json_parser(data):
    with open(data) as data_open:
        data = json.loads(data_open.read())
    return data
spells_data = json_parser('spells.json')

class Spell:
    def __init__(self, query):
        self.name = query
        self.att_dict = self.get_dict(self.name)
        self.desc = self.get_att('desc')
        self.page = self.get_att('page')
        self.range = self.get_att('range')
        self.components = self.get_att('components')
        # this doesn't work for some reason: self.material = self.get_att('material')
        self.ritual = self.get_att('ritual')
        self.duration = self.get_att('duration')
        self.concentration = self.get_att('concentration')
        self.casting_time = self.get_att('casting_time')
        self.level = self.get_att('level')
        self.school = self.get_att('school')
        self.classes = self.get_att('classes')

    def get_dict(self, query):
        return next(item for item in spells_data if item["name"] == query)
            
    def get_att(self, att):
        return self.att_dict[att]

text = "input the spell you'd like to look up followed by the attribute you want to retrieve"
print(text)
string = input(">").split(', ')


print(Spell(string[0]).__dict__[string[1]])
