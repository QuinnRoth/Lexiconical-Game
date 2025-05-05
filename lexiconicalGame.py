import re
import json
import requests
import os
from dotenv import load_dotenv

"""
Game Rules:
    Goal: Enter a word that follows as many rules as possible.
    There are 5ish rules for the word to follow
    No googling
    Game starts by only showing you the first rule
    When you enter a word that follows the new rule a new rule appears
"""
word = "insouciance"
load_dotenv()
api_key = os.getenv("API_KEY")


def checkAnswer(test):

    if re.search(r"([^a-zA-Z])", test):
        print("Invalid Word in first if")
        return False



    # API url
    url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + test + "?key=" + api_key
    try:
        response = requests.get(url)  # get response
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    data = response.json()  # get the json data

    # Assuming the first definition is the most relevant
    try:
        for entry in data:
            if isinstance(entry, dict) and 'meta' in entry and entry['meta']:  # if the word is in the dictionary
                return True
            else:
                print("Invalid Word isinstance")
                return False
    except AttributeError:  # for any errors
        print("Invalid Word attribute error")
        return False


def checkRules(test):

    rule1 = re.search(r"ou", test)
    if rule1:
        rule2 = re.search(r"i.*i", test)
        if rule2:
            rule3 = re.search(r"^[aeiouy].*[aeiouy]$", test)
            if rule3:
                rule4 = re.search(r"(.*){12}", test)
                if rule4:
                    rule5 = re.search("insouciance", test)
                    if rule5:
                        return 5
                    return 4
                return 3
            return 2
        return 1
    else:
        return 0

def printRules(num):
    if num > 4:
        print("Congrats you got today's word!")
    if num > 3:
        print("Rule 5: Guess today's word!")
    if num > 2:
        print("Rule 4: Must be 11 characters long.")
    if num > 1:
        print("Rule 3: The beginning and end must both be vowels.")
    if num > 0:
        print("Rule 2: Must include the letter 'i' twice.")
    print("Rule 1: Must Include the letter combination 'ou'.")


score = 0

while 1:
    printRules(score)
    print("Enter a word that follows the rules or blank if you wold like to quit.")
    answer = input()
    if answer == "":
        quit(0)
    if checkAnswer(answer):
        score = checkRules(answer)
        print(score)

