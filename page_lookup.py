##
## This code is old and no longer in use, but I'm keeping it for reference
##

import json
import sys, json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

startup_text = "Welcome to 5e page lookup. What are you looking for?"
reprompt_text = "\nWhat else would you like to search for? Type EXIT to exit"

data = {}
with open('PHB.json') as f:
    data = json.loads(f.read().lower())

def startup():
    print(startup_text)
    lookup()

def reprompt():
    print(reprompt_text)
    lookup()

def fuzzymatch(string):
    print(f"No match found for {string}. Were you looking one of these?\n")
    name_dict = []
    for entry in data:
        name_dict.append(entry["name"])
    fuzzy_tuples = process.extract(string, name_dict, limit=25)
    fuzzy_list = [x[0] for x in fuzzy_tuples if x[1] > 60]
    for x in fuzzy_list:
        print(x)
    reprompt()

def lookup(): #FIXME: get output to have proper capitalization
    string = input(">")
    if string == 'EXIT':
        exit(0)

    print(' ')
    lookup_list = []

    for x in data: # fuzz
        if string.lower() in x.get('name'):
            lookup_list.append(x)
    if lookup_list != []:
        display_results(lookup_list)
    else:
        fuzzymatch(string)


def display_results(list):
    for x in list:
        print('Topic: ', x.get('name'))
        print('\tPages: ', ', '.join([str(p) for p in x.get('pages', [])]))

    reprompt()

def debug():
    string = input(">")
    fuzzy_tuples = process.extractBests(string, data)
    fuzzy_list = [x[0] for x in fuzzy_tuples if x[1] > 60]
    print(fuzzy_tuples)
    print(fuzzy_list)
    debug()

#debug()

startup()
