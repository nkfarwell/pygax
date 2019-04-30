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

def fuzzymatch():
    string = input(">")
    fuzzy_tuples = process.extract(string, data, limit=3)
    fuzzy_list = [x[0] for x in fuzzy_tuples]
    display_results(fuzzy_list)

def lookup(): #FIXME: get output to have proper capitalization
    string = input(">")
    if string == 'EXIT':
        exit(0)

    print(' ')
    lookup_list = []

    for x in data: # fuzz
        if string.lower() in x.get('name'):
            lookup_list.append(x)
    display_results(lookup_list)

    fuzzy_tuples = process.extract(string, data, limit=3)
    fuzzy_list = [x[0] for x in fuzzy_tuples]
    print(fuzzy_list)
    display_results(fuzzy_list)

def display_results(list):
    for x in list:
        print('Topic: ', x.get('name'))
        print('\tPages: ', ', '.join([str(p) for p in x.get('pages', [])]))

    reprompt()

#startup()
fuzzymatch()
